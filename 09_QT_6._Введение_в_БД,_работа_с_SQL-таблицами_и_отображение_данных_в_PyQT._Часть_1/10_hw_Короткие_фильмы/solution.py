import sqlite3

QUERY = """
SELECT title FROM Films WHERE duration <= 85
"""


def main():
    name = input()
    con = sqlite3.connect(name)
    for row in con.execute(QUERY):
        print(row[0])
    con.close()


if __name__ == "__main__":
    main()
