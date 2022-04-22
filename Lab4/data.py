import sqlite3

def create():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("create table sensor_data (id INTEGER PRIMARY KEY AUTOINCREMENT, temperature FLOAT, time DATETIME default current_timestamp);")
    conn.commit()
    conn.close()

def insert(temperature):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO sensor_data (temperature) VALUES (%.2f)" % temperature )

    conn.commit()
    conn.close()


def drop():
    conn =sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("drop table sensor_data")
    conn.commit()
    conn.close()


def select():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    cursor = c.execute("SELECT temperature, time from sensor_data")
    rows = cursor.fetchall()
    conn.close()
    return rows
