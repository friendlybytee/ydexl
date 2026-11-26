import csv


def main():
    n = float(input())
    with open("vps.csv", encoding="utf-8") as f:
        rows = list(csv.reader(f, delimiter=";"))
    for r in rows[1:]:
        if float(r[4]) >= n:
            print(r[0])


if __name__ == "__main__":
    main()
