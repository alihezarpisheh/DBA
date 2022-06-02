import sqlite3


def connect():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text, author text,year integer,
    isbn integer)""")
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM BOOK")
    r = cursor.fetchall()
    connection.close()
    return r


def search(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    r = cursor.fetchall()
    connection.close()
    return r


def add(title, author, year, isbn):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def edit(id, title, author, year, isbn):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    connection.commit()
    connection.close()


def delete(id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    connection.commit()
    connection.close()


connect()

