def arsenal(*args):
    avg = sum(len(a) for a in args) / len(args)
    return sorted({a.capitalize() for a in args if len(a) <= avg})
