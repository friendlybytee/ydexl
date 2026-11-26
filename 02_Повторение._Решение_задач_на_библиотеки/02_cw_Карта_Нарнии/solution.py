import os

a = []
if os.path.isdir('narnia_map'):
    a = sorted(f for f in os.listdir('narnia_map') if f.endswith('.txt'))
if not a:
    print('Карта ещё не создана!')
else:
    for f in a:
        print(f)
    print(f'Всего файлов txt: {len(a)}')
