def scrolls(*args):
    return sorted([a for a, b in args if 'elves' in b.lower()], reverse=True)
