import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    con.execute("UPDATE films SET duration = duration / 3 WHERE year = 1973")
    con.commit()
    con.close()
