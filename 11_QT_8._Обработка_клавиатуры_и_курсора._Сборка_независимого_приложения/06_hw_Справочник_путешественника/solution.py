import sqlite3


def main():
    con = sqlite3.connect("database.sql")
    cur = con.cursor()
    cur.executescript("""
    DROP TABLE IF EXISTS Countries;
    DROP TABLE IF EXISTS Languages;
    CREATE TABLE Languages (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);
    CREATE TABLE Countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        language INTEGER REFERENCES Languages(id),
        year INTEGER,
        flag TEXT
    );
    INSERT INTO Languages (name) VALUES ('Английский'), ('Французский'), ('Русский'), ('Немецкий');
    INSERT INTO Countries (name, language, year, flag) VALUES
        ('Великобритания', 1, 1707, '🇬🇧'),
        ('США', 1, 1776, '🇺🇸'),
        ('Австралия', 1, 1901, '🇦🇺'),
        ('Франция', 2, 843, '🇫🇷'),
        ('Россия', 3, 1721, '🇷🇺'),
        ('Германия', 4, 1871, '🇩🇪');
    """)
    con.commit()
    con.close()


if __name__ == "__main__":
    main()
