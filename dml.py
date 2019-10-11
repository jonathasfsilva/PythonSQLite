import sqlite3

def db_insert(nome, fone, email):
    sqlStr = """
    INSERT INTO users (name, phone, email)
    VALUES('{}', '{}', '{}')
    """.format(nome, fone, email)
    cursor.execute(sqlStr)
    con.commit()

con = sqlite3.connect('base.db')

cursor = con.cursor()

db_insert("juvenal", "92292323", "juju@venal.com")

con.close()
