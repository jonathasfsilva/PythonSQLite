import sqlite3

def createDataBase():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    sqlStr = """
    CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL)"""
    try:
        cursor.execute(sqlStr)
        con.commit()
    except Exception as e:
        raise
    con.close()

createDataBase()
