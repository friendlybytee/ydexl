import sqlite3

QUERY = """
SELECT f.title FROM Films f JOIN genres g ON g.id = f.genre
WHERE g.title = 'детектив' AND f.year BETWEEN 1995 AND 2000
"""


def main():
    name = input()
    con = sqlite3.connect(name)
    for row in con.execute(QUERY):
        print(row[0])
    con.close()


if __name__ == "__main__":
    main()
