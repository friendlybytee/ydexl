import csv


def main():
    school, cls = map(int, input().split())
    with open("rez.csv", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    res = []
    for r in rows[1:]:
        p = r[2].split("-")
        if int(p[2]) == school and int(p[3]) == cls:
            res.append((r[1].split()[3], int(r[7])))
    res.sort(reverse=True)
    res.sort(key=lambda a: a[1], reverse=True)
    for name, score in res:
        print(name, score)


if __name__ == "__main__":
    main()
