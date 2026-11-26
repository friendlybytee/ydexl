import csv


def load_kings(filename):
    with open(filename, encoding='utf-8') as f:
        return [(r['king'], int(r['start_year']), int(r['end_year']))
                for r in csv.DictReader(f, delimiter=';')]


def filter_by_century(kings, century):
    a = (century - 1) * 100 + 1
    b = century * 100
    return sorted(k[0] for k in kings if k[1] <= b and k[2] >= a)


def longest_ruling(kings, n):
    lst = sorted(kings, key=lambda k: (-(k[2] - k[1] + 1), k[0]))
    return [k[0] for k in lst[:n]]


def report(kings):
    avg = sum(k[2] - k[1] + 1 for k in kings) // len(kings)
    return (f'Всего правителей: {len(kings)}\n'
            f'Средняя длина правления: {avg} лет\n'
            f'Самый долгий правитель: {longest_ruling(kings, 1)[0]}')
