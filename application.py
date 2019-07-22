import sqlite3

path = '/home/jonathas/development/database-py-sqlite/'

conn = sqlite3.connect(path+'database.db')

print(type(conn))

conn.close()