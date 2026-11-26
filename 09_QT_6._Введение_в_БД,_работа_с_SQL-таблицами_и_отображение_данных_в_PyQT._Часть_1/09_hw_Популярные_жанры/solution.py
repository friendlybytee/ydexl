import sqlite3

con = sqlite3.connect(input())
for r in con.execute("SELECT title FROM genres WHERE id IN (SELECT genre FROM Films WHERE year IN (2010, 2011))"):
    print(r[0])
