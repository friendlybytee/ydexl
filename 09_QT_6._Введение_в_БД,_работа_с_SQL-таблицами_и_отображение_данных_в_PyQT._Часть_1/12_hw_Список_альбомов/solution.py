import sqlite3

QUERY = """
SELECT DISTINCT al.Title FROM Album al
JOIN Track t ON t.AlbumId = al.AlbumId
JOIN Genre g ON g.GenreId = t.GenreId
WHERE g.Name = ?
ORDER BY al.ArtistId, al.Title
"""


def main():
    value = input()
    con = sqlite3.connect("music_db.sqlite")
    for row in con.execute(QUERY, (value,)):
        print(row[0])
    con.close()


if __name__ == "__main__":
    main()
