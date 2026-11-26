v = 'aeiou'
s = input()
while s:
    a = s.lower()
    if len(a) < 4:
        print('Слишком короткое.')
    elif len(a) >= 20:
        print('Слишком длинное.')
    elif a[0] not in v:
        print('Неверное начало.')
    elif a[-1] in v:
        print('Неверный конец.')
    else:
        r = 'Красиво!'
        for i in range(len(a) - 1):
            if a[i] in v and a[i + 1] in v:
                r = f'Две гласные {a[i:i + 2]} подряд.'
                break
        print(r)
    s = input()
