import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    con.execute("DELETE FROM films WHERE title LIKE 'Я%' AND title LIKE '%а'")
    con.commit()
    con.close()
