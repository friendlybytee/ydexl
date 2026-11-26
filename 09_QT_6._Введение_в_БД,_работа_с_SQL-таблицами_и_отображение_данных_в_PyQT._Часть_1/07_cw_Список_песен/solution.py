import sqlite3

QUERY = """
SELECT DISTINCT t.Name FROM Track t
JOIN Album al ON al.AlbumId = t.AlbumId
JOIN Artist ar ON ar.ArtistId = al.ArtistId
WHERE ar.Name = ?
ORDER BY t.Name
"""


def main():
    value = input()
    con = sqlite3.connect("music_db.sqlite")
    for row in con.execute(QUERY, (value,)):
        print(row[0])
    con.close()


if __name__ == "__main__":
    main()
