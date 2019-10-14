import sqlite3

def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('base.db')
        cursor = con.cursor()
        sql = func(*args)
        cursor.execute(sql)
        con.commit()
        con.close()
    return decorator

@commit_close
def db_insert(nome, fone, email):
    return """
    INSERT INTO users (name, phone, email)
    VALUES('{}', '{}', '{}')
    """.format(nome, fone, email)

@commit_close
def db_update(nome, email):
    return """
    UPDATE users SET name = '{}' WHERE email = '{}'
    """.format(nome, email)

@commit_close
def db_delete(email):
    return """
    DELETE FROM users WHERE email = '{}'
    """.format(email)

def db_select(data, field):
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    sql = """
    SELECT name, email, phone
    FROM users
    WHERE {} == '{}' """.format(field, data)
    cursor.execute(sql)
    data = cursor.fetchone()
    con.close()
    return data
