import csv
import json


def process_treasures(csv_filename, json_filename, secret_key, grouping):
    names = {'Предмет': 'Item', 'Количество': 'Quantity',
             'Цена_в_золотых': 'Price_in_gold', 'Где_найдено': 'Found_in'}
    grouping = names.get(grouping, grouping)
    with open(csv_filename, encoding='utf-8') as f:
        rows = list(csv.DictReader(f, delimiter='.'))
    if sum(int(r['Quantity']) for r in rows) != int(secret_key):
        res = {'error': 'access denied'}
    else:
        g = {}
        for r in rows:
            k = r[grouping]
            if k not in g:
                g[k] = {'total_items': 0, 'total_value': 0, 'items': []}
            q = int(r['Quantity'])
            g[k]['total_items'] += q
            g[k]['total_value'] += q * int(r['Price_in_gold'])
            g[k]['items'].append(r['Item'])
        res = {}
        for k in sorted(g):
            g[k]['items'].sort(reverse=True)
            res['group' + k] = g[k]
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
