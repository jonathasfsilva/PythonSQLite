import sqlite3

con = sqlite3.connect('base.db')

cursor = con.cursor()

sqlStr = """
CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
phone TEXT NOT NULL,
email TEXT UNIQUE NOT NULL)"""

cursor.execute(sqlStr)
con.commit()
con.close()
