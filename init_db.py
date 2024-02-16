import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

cur.execute("""CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    autor TEXT NOT NULL,
    titulo TEXT NOT NULL,
    posteo TEXT NOT NULL
)""")

cur.execute("""CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)""")

connection.commit()

connection.close()