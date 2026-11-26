def travel(fname, key=max):
    with open(fname, encoding='utf-8') as f:
        m = [list(map(int, s.split())) for s in f if s.strip()]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i and j:
                m[i][j] += key(m[i - 1][j], m[i][j - 1])
            elif i:
                m[i][j] += m[i - 1][j]
            elif j:
                m[i][j] += m[i][j - 1]
    return m[-1][-1]
