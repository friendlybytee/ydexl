def path(lst, criterion):
    res = []
    for a in lst:
        if criterion(a):
            break
        res.append(a)
    if lst and not res:
        return 'Danger!'
    return ', '.join(res)
