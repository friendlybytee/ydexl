import sqlite3

QUERY = """
SELECT DISTINCT year FROM Films WHERE title LIKE 'Х%'
"""


def main():
    name = input()
    con = sqlite3.connect(name)
    for row in con.execute(QUERY):
        print(row[0])
    con.close()


if __name__ == "__main__":
    main()
