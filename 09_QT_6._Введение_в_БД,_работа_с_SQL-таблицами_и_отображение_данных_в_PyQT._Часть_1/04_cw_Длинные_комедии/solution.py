import sqlite3

QUERY = """
SELECT f.title FROM Films f JOIN genres g ON g.id = f.genre
WHERE g.title = 'комедия' AND f.duration >= 60
"""


def main():
    name = input()
    con = sqlite3.connect(name)
    for row in con.execute(QUERY):
        print(row[0])
    con.close()


if __name__ == "__main__":
    main()
