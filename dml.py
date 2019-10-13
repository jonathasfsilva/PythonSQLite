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

def db_delete(email):
    return """
    DELETE FROM users WHERE email = '{}'
    """.format(email)

def db_select(data, field):
    return """
    SELECT id, name, phone, email
    FROM users
    WHERE {}={}""".format(field, data)
