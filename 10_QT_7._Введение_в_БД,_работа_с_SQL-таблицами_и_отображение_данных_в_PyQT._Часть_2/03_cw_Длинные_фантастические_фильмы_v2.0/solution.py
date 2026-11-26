import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    con.execute("UPDATE films SET duration = duration * 2 WHERE genre = (SELECT id FROM genres WHERE title = 'фантастика')")
    con.commit()
    con.close()
