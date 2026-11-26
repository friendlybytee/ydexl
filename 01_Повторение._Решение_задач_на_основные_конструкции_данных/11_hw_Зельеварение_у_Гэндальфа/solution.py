def potions(s):
    res = []
    with open('recipes.txt', encoding='utf-8') as f:
        for line in f:
            a = line.strip().split(',')
            if s.lower() in a[0].lower():
                res = a[1:]
    return res
