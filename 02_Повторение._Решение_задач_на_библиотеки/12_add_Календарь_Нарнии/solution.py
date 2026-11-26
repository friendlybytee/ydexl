from datetime import datetime, timedelta

w = ['Понд', 'Вторнд', 'Тринд', 'Четв', 'Пятн', 'Шестн', 'Седьмидень', 'Восьмидень']
m = ['Лев', 'Колдунья', 'Фавн', 'Бобр', 'Кентавр', 'Орланд', 'Древо', 'Фонарь', 'Дуб']
h = ['День Творения', 'День Пробуждения', 'День Даров', 'День Пророчества', 'День Возвращения']
r = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


def main():
    a = datetime.strptime(input().strip(), '%d.%m.%Y')
    s = input().strip()
    if s in h:
        n = 360 + h.index(s)
        print(h.index(s) + 1)
    else:
        d, mn = s.split()
        n = m.index(mn) * 40 + int(d) - 1
        print(w[n % 8])
    b = a + timedelta(days=n)
    print(f'{r[b.weekday()]}, {b.strftime("%d.%m.%Y")}')


if __name__ == "__main__":
    main()
