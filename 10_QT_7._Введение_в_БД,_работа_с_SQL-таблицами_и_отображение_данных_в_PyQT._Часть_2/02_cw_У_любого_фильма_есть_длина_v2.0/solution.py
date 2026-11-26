import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    con.execute("UPDATE films SET duration = 42 WHERE duration = ''")
    con.commit()
    con.close()
