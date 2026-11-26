import sqlite3


def main():
    con = sqlite3.connect("database.sql")
    cur = con.cursor()
    cur.executescript("""
    DROP TABLE IF EXISTS Items;
    DROP TABLE IF EXISTS Types;
    DROP TABLE IF EXISTS Spaces;
    CREATE TABLE Types (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);
    CREATE TABLE Spaces (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);
    CREATE TABLE Items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type INTEGER REFERENCES Types(id),
        year INTEGER,
        space INTEGER REFERENCES Spaces(id)
    );
    INSERT INTO Types (name) VALUES ('Мебель'), ('Бытовая техника'), ('Посуда');
    INSERT INTO Spaces (name) VALUES ('Кухня'), ('Гостиная'), ('Спальня');
    INSERT INTO Items (name, type, year, space) VALUES
        ('Холодильник', 2, 2018, 1),
        ('Микроволновка', 2, 2020, 1),
        ('Стол обеденный', 1, 2015, 1),
        ('Диван', 1, 2019, 2),
        ('Телевизор', 2, 2021, 2),
        ('Кровать', 1, 2017, 3),
        ('Шкаф', 1, 2016, 3),
        ('Сервиз', 3, 2014, 2);
    """)
    con.commit()
    con.close()


if __name__ == "__main__":
    main()
