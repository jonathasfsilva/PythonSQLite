import sqlite3

def db_insert(nome, fone, email):
    return """
    INSERT INTO users (name, phone, email)
    VALUES('{}', '{}', '{}')
    """.format(nome, fone, email)

def db_update(nome, email):
    return """
    UPDATE users SET name = '{}' WHERE email = '{}'
    """.format(nome, email)

con = sqlite3.connect('base.db')

cursor = con.cursor()

con.execute(db_update("Jonathas F Silva", "jonathas@gmail.com"))

con.commit()
con.close()
