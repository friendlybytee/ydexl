import os
import sys
import io
import re
import json
import time
import subprocess
import urllib.parse
import requests
import websocket
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Set stdout to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

COURSE_ID = 1722
GROUP_ID = 56965
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BROWSER_PROFILE = os.path.join(os.path.expanduser('~'), '.ydexl_browser')
PORT = 9222
BROWSERS = [
    r'%ProgramFiles%\BraveSoftware\Brave-Browser\Application\brave.exe',
    r'%ProgramFiles(x86)%\BraveSoftware\Brave-Browser\Application\brave.exe',
    r'%LocalAppData%\BraveSoftware\Brave-Browser\Application\brave.exe',
    r'%ProgramFiles%\Google\Chrome\Application\chrome.exe',
    r'%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe',
    r'%LocalAppData%\Google\Chrome\Application\chrome.exe',
    '/usr/bin/brave-browser',
    '/usr/bin/google-chrome',
]

TAG_MAP = {
    'classwork': ('cw', 'Классная работа'),
    'homework': ('hw', 'Домашняя работа'),
    'additional': ('add', 'Дополнительные задачи'),
    'control-work': ('ctrl', 'Самостоятельная работа'),
    'feedback-2': ('feedback', 'Обратная связь'),
}

def find_browser():
    for p in BROWSERS:
        p = os.path.expandvars(p)
        if os.path.exists(p):
            return p
    sys.exit('[!] Не найден ни Brave, ни Chrome')

def get_cookies(headless):
    args = [find_browser(), f'--remote-debugging-port={PORT}', f'--user-data-dir={BROWSER_PROFILE}', '--no-first-run']
    if headless:
        args += ['--headless=new', 'about:blank']
    else:
        args.append('https://lms.yandex.ru/')
    proc = subprocess.Popen(args)

    ws_url = None
    for _ in range(50):
        try:
            ws_url = requests.get(f'http://127.0.0.1:{PORT}/json/version', timeout=1).json()['webSocketDebuggerUrl']
            break
        except requests.RequestException:
            time.sleep(0.2)
    if not ws_url:
        proc.kill()
        sys.exit('[!] Не удалось подключиться к браузеру')

    if not headless:
        input('[*] Войдите в аккаунт на lms.yandex.ru в открывшемся окне и нажмите Enter...')

    ws = websocket.create_connection(ws_url, suppress_origin=True)
    ws.send(json.dumps({'id': 1, 'method': 'Storage.getCookies'}))
    cookies = json.loads(ws.recv())['result']['cookies']
    ws.send(json.dumps({'id': 2, 'method': 'Browser.close'}))
    ws.close()
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
    return [c for c in cookies if 'yandex' in c['domain']]

def make_session(cookies):
    session = requests.Session()
    for c in cookies:
        session.cookies.set(c['name'], c['value'], domain=c['domain'], path=c['path'])
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
    })
    return session

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', '_', name)
    name = re.sub(r'\s+', '_', name).strip('_')
    return name

def clean_markdown(text):
    if not text:
        return ''
    # Normalize multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def download_file(session, url, target_path):
    try:
        r = session.get(url, stream=True, timeout=15)
        if r.status_code == 200:
            with open(target_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
    except Exception as e:
        print(f"    [!] Ошибка при скачивании {url}: {e}")
    return False

def parse_and_process_task(session, html, task_dir, task_title):
    soup = BeautifulSoup(html, 'html.parser')
    os.makedirs(task_dir, exist_ok=True)

    # 1. Download images & replace src
    img_counter = 1
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src.startswith('http') or src.startswith('//'):
            if src.startswith('//'):
                src = 'https:' + src
            ext = os.path.splitext(urllib.parse.urlparse(src).path)[1]
            if not ext:
                ext = '.png'
            base_name = os.path.basename(urllib.parse.urlparse(src).path)
            if not base_name or len(base_name) < 3:
                img_name = f'image_{img_counter}{ext}'
            else:
                img_name = sanitize_filename(base_name)
            img_path = os.path.join(task_dir, img_name)
            if download_file(session, src, img_path):
                img['src'] = f'./{img_name}'
            img_counter += 1

    # 2. Download downloadable attachments & replace href
    file_extensions = ('.ui', '.csv', '.sqlite', '.db', '.txt', '.zip', '.json', '.py', '.xlsx', '.pdf')
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href.startswith('http') or href.startswith('//'):
            if href.startswith('//'):
                href = 'https:' + href
            text = a.get_text(strip=True)
            url_path = urllib.parse.urlparse(href).path
            is_file = any(url_path.lower().endswith(ext) or text.lower().endswith(ext) for ext in file_extensions)
            if is_file or 'yastatic.net/s3/lyceum' in href:
                # determine filename
                fname = None
                for ext in file_extensions:
                    if text.lower().endswith(ext):
                        fname = sanitize_filename(text)
                        break
                if not fname:
                    fname = os.path.basename(url_path)
                if fname:
                    target_file = os.path.join(task_dir, fname)
                    if download_file(session, href, target_file):
                        a['href'] = f'./{fname}'

    # 3. Extract limits table
    limits = {}
    header_table = soup.find('table')
    if header_table:
        for tr in header_table.find_all('tr'):
            tds = tr.find_all('td')
            if len(tds) == 2:
                prop = tds[0].get_text(strip=True)
                val = tds[1].get_text(strip=True).replace('\xa0', ' ')
                limits[prop] = val

    # 4. Extract legend
    legend_el = soup.find(class_='legend')
    legend_md = clean_markdown(md(str(legend_el), heading_style='ATX')) if legend_el else ''

    # 5. Extract input & output specifications
    in_el = soup.find(class_='input-specification')
    in_md = clean_markdown(md(str(in_el), heading_style='ATX')) if in_el else ''

    out_el = soup.find(class_='output-specification')
    out_md = clean_markdown(md(str(out_el), heading_style='ATX')) if out_el else ''

    # 6. Extract samples
    samples = []
    for sample_table in soup.find_all('table', class_='sample-tests'):
        # Skip if table is actually the limits header table
        if sample_table.find(class_=['time-limit', 'memory-limit', 'property-title']):
            continue
        tbody = sample_table.find('tbody') or sample_table
        for row in tbody.find_all('tr'):
            if row.find(class_=['time-limit', 'memory-limit', 'property-title']):
                continue
            cols = row.find_all('td')
            if len(cols) >= 2:
                inp = cols[0].find('pre')
                outp = cols[1].find('pre')
                inp_text = inp.get_text() if inp else cols[0].get_text()
                outp_text = outp.get_text() if outp else cols[1].get_text()
                samples.append((inp_text.strip('\r\n'), outp_text.strip('\r\n')))

    # 7. Extract notes
    notes_el = soup.find(class_='notes')
    notes_md = clean_markdown(md(str(notes_el), heading_style='ATX')) if notes_el else ''

    # Fallback if standard classes not present
    if not legend_md and not in_md:
        body = soup.find(class_='problem-statement') or soup
        for t in body.find_all('table', class_='sample-tests'):
            t.decompose()
        if header_table:
            header_table.decompose()
        legend_md = clean_markdown(md(str(body), heading_style='ATX'))

    return limits, legend_md, in_md, out_md, samples, notes_md

def generate_task_readme(task_meta, limits, legend, in_md, out_md, samples, notes):
    tag_info = TAG_MAP.get(task_meta.get('tag', {}).get('type', ''), ('', task_meta.get('tag', {}).get('type', '')))
    
    lines = []
    lines.append(f"# {task_meta.get('title')}\n")
    lines.append("| Характеристика | Значение |")
    lines.append("| --- | --- |")
    lines.append(f"| **Категория** | {tag_info[1]} |")
    lines.append(f"| **Макс. балл** | {task_meta.get('scoreMax', '-')} |")
    if 'Ограничение времени' in limits:
        lines.append(f"| **Ограничение времени** | {limits['Ограничение времени']} |")
    if 'Ограничение памяти' in limits:
        lines.append(f"| **Ограничение памяти** | {limits['Ограничение памяти']} |")
    if 'Ввод' in limits:
        lines.append(f"| **Ввод** | {limits['Ввод']} |")
    if 'Вывод' in limits:
        lines.append(f"| **Вывод** | {limits['Вывод']} |")
    lines.append(f"| **ID задачи** | `{task_meta.get('id')}` |")
    lines.append("\n---\n")

    if legend:
        lines.append("## Условие\n")
        lines.append(f"{legend}\n")

    if in_md:
        lines.append("## Формат ввода\n")
        lines.append(f"{in_md}\n")

    if out_md:
        lines.append("## Формат вывода\n")
        lines.append(f"{out_md}\n")

    if samples:
        lines.append("## Примеры\n")
        for i, (inp, outp) in enumerate(samples, 1):
            lines.append(f"### Пример {i}\n")
            lines.append("**Ввод:**")
            lines.append("```")
            lines.append(inp)
            lines.append("```\n")
            lines.append("**Вывод:**")
            lines.append("```")
            lines.append(outp)
            lines.append("```\n")

    if notes:
        lines.append("## Примечания\n")
        lines.append(f"{notes}\n")

    return '\n'.join(lines)

def generate_solution_template(task_meta, limits, legend, in_md, out_md, samples):
    tag_info = TAG_MAP.get(task_meta.get('tag', {}).get('type', ''), ('', task_meta.get('tag', {}).get('type', '')))
    
    # Docstring summary
    doc_lines = []
    doc_lines.append(f"Задача: {task_meta.get('title')}")
    doc_lines.append(f"Категория: {tag_info[1]}")
    if 'Ограничение времени' in limits:
        doc_lines.append(f"Ограничение времени: {limits['Ограничение времени']}")
    if 'Ограничение памяти' in limits:
        doc_lines.append(f"Ограничение памяти: {limits['Ограничение памяти']}")
    doc_lines.append("")
    
    # Add truncated or full legend text
    if legend:
        doc_lines.append("Условие:")
        for l in legend.splitlines():
            doc_lines.append(l)
        doc_lines.append("")

    if in_md:
        doc_lines.append("Формат ввода:")
        for l in in_md.splitlines():
            doc_lines.append(l)
        doc_lines.append("")

    if out_md:
        doc_lines.append("Формат вывода:")
        for l in out_md.splitlines():
            doc_lines.append(l)
        doc_lines.append("")

    if samples:
        doc_lines.append("Пример:")
        for i, (inp, outp) in enumerate(samples[:2], 1):
            doc_lines.append(f"--- Пример {i} ---")
            doc_lines.append(f"Ввод:\n{inp}")
            doc_lines.append(f"Вывод:\n{outp}")
            doc_lines.append("")

    doc_text = '\n'.join(doc_lines).replace('"""', "'''")
    
    code = f'"""\n{doc_text}\n"""\n\nimport sys\n\n\ndef main():\n    # TODO: вайбкодинг решения начинается здесь\n    pass\n\n\nif __name__ == "__main__":\n    main()\n'
    return code

def main():
    lessons_url = f'https://lms.yandex.ru/api/student/lessons?courseId={COURSE_ID}&groupId={GROUP_ID}'

    print("[*] Чтение cookies из браузера...")
    session = make_session(get_cookies(headless=True))

    print(f"[*] Получение списка уроков курса {COURSE_ID} (группа {GROUP_ID})...")
    resp = session.get(lessons_url, allow_redirects=False)
    if resp.status_code != 200:
        print("[*] Нужен вход в Яндекс")
        session = make_session(get_cookies(headless=False))
        resp = session.get(lessons_url, allow_redirects=False)
    if resp.status_code != 200:
        print(f"[!] Ошибка запроса уроков: {resp.status_code}")
        return

    lessons = resp.json()
    print(f"[+] Найдено уроков: {len(lessons)}")

    course_toc = []
    total_tasks_count = 0

    for l_idx, lesson in enumerate(lessons, 1):
        l_id = lesson['id']
        l_title = lesson['title']
        l_dir_name = f"{l_idx:02d}_{sanitize_filename(l_title)}"
        l_dir = os.path.join(BASE_DIR, l_dir_name)
        os.makedirs(l_dir, exist_ok=True)

        print(f"\n[{l_idx}/{len(lessons)}] Урок {l_idx}: {l_title}")
        
        # Get tasks for lesson
        tasks_resp = session.get(f'https://lms.yandex.ru/api/student/tasks?lessonId={l_id}&courseId={COURSE_ID}&groupId={GROUP_ID}')
        if tasks_resp.status_code != 200:
            print(f"  [!] Ошибка при получении задач урока {l_id}: {tasks_resp.status_code}")
            continue

        tasks_list = tasks_resp.json().get('results', [])
        print(f"  Найдено задач: {len(tasks_list)}")
        total_tasks_count += len(tasks_list)

        lesson_toc = []

        for t_idx, task in enumerate(tasks_list, 1):
            t_id = task['id']
            t_title = task.get('title', f'Task_{t_id}')
            tag_type = task.get('tag', {}).get('type', 'task')
            tag_prefix, tag_name = TAG_MAP.get(tag_type, (tag_type[:4], tag_type))

            t_dir_name = f"{t_idx:02d}_{tag_prefix}_{sanitize_filename(t_title)}"
            t_dir = os.path.join(l_dir, t_dir_name)
            os.makedirs(t_dir, exist_ok=True)

            print(f"  [{t_idx:02d}/{len(tasks_list):02d}] {tag_prefix.upper()} | {t_title} (ID: {t_id})")

            # Fetch detailed task
            det_resp = session.get(f'https://lms.yandex.ru/api/student/tasks/{t_id}?groupId={GROUP_ID}')
            if det_resp.status_code != 200:
                print(f"    [!] Ошибка загрузки описания задачи {t_id}: {det_resp.status_code}")
                continue

            det_data = det_resp.json()
            html = det_data.get('description', '')

            # Parse & download images/files
            limits, legend, in_md, out_md, samples, notes = parse_and_process_task(session, html, t_dir, t_title)

            # Generate task README.md
            task_readme = generate_task_readme(det_data, limits, legend, in_md, out_md, samples, notes)
            with open(os.path.join(t_dir, 'README.md'), 'w', encoding='utf-8') as f:
                f.write(task_readme)

            # Generate solution.py template
            solution_code = generate_solution_template(det_data, limits, legend, in_md, out_md, samples)
            sol_path = os.path.join(t_dir, 'solution.py')
            if not os.path.exists(sol_path):
                with open(sol_path, 'w', encoding='utf-8') as f:
                    f.write(solution_code)

            lesson_toc.append({
                'num': t_idx,
                'tag': tag_name,
                'tag_prefix': tag_prefix,
                'title': t_title,
                'score': det_data.get('scoreMax', '-'),
                'dir': t_dir_name,
            })

        # Generate lesson README.md
        lesson_readme_lines = [
            f"# {l_title}\n",
            f"**Курс:** Промышленное программирование на Python | 26/27  ",
            f"**ID урока:** `{l_id}`  ",
            f"**Всего задач:** {len(lesson_toc)}\n",
            "## Список заданий\n",
            "| № | Тип | Название | Балл | Папка с решением |",
            "|---|---|---|---|---|",
        ]
        for item in lesson_toc:
            lesson_readme_lines.append(
                f"| {item['num']} | {item['tag']} | [{item['title']}](./{item['dir']}/README.md) | {item['score']} | [{item['dir']}](./{item['dir']}/) |"
            )
        lesson_readme_lines.append("\n---\n*Сгенерировано автоматически с lms.yandex.ru*")

        with open(os.path.join(l_dir, 'README.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(lesson_readme_lines))

        course_toc.append({
            'num': l_idx,
            'id': l_id,
            'title': l_title,
            'tasks_count': len(lesson_toc),
            'dir': l_dir_name,
        })

    # Generate master README.md
    master_lines = [
        "# Яндекс.Лицей: Промышленное программирование на Python (2026/2027)\n",
        f"Репозиторий с текстами заданий, прикрепленными файлами и заготовками для вайбкодинга решений.\n",
        f"**Всего уроков:** {len(course_toc)}  ",
        f"**Всего задач:** {total_tasks_count}\n",
        "## Содержание курса\n",
        "| № | Урок | Задач | Ссылка |",
        "|---|---|---|---|",
    ]
    for c_item in course_toc:
        master_lines.append(
            f"| {c_item['num']:02d} | [{c_item['title']}](./{c_item['dir']}/README.md) | {c_item['tasks_count']} | [Перейти к уроку](./{c_item['dir']}/) |"
        )
    master_lines.append("\n## Структура каждой задачи\n")
    master_lines.append("В папке каждой задачи находятся:")
    master_lines.append("- `README.md` — полное условие, форматы ввода/вывода, ограничения и примеры тестов.")
    master_lines.append("- `solution.py` — заготовка кода с условием в docstring (готова к запуску и решению).")
    master_lines.append("- Скачанные ресурсы задачи (файлы `.ui`, базы данных `.sqlite`/`.db`, датасеты `.csv`, демонстрационные `.gif`/`.png`).\n")
    master_lines.append("---\n*Приятного вайбкодинга!*")

    with open(os.path.join(BASE_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(master_lines))

    print(f"\n[OK] Экспорт завершен! Собрано {total_tasks_count} задач по {len(course_toc)} урокам.")

if __name__ == '__main__':
    main()
