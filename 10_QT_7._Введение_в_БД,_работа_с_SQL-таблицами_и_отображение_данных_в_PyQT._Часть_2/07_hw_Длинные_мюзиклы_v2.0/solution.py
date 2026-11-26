import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    con.execute("UPDATE films SET duration = 100 WHERE genre = (SELECT id FROM genres WHERE title = 'мюзикл') AND duration > 100")
    con.commit()
    con.close()
