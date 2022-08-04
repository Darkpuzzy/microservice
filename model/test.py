import sqlite3
import datetime
from connect import timet


URL_DB = '../mydata2.db'

time = datetime.datetime.now()
time_str = time.strftime('%Y-%m-%d %H:%m:%S')

connect = sqlite3.connect('../mydata2.db')
FK = connect.execute("PRAGMA foreign_keys = true")

def init_database():
    with connect as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE books(
        Id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        count_page INTEGER NOT NULL CHECK (count_page >0),
        price REAL CHECK (price >0),
        auth_id INTEGER NOT NULL,
        FOREIGN KEY (auth_id) REFERENCES auth(id)
        )""")
        db.commit()


def second_database():
    with connect as db:
        cursor = db.cursor()
        cursor.execute(""" CREATE TABLE auth(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER  CHECK (age >16)
        )""" )
        db.commit()

def insert_aut():
    with connect as db:
        FK
        cursor = db.cursor()
        cursor.execute(""" INSERT INTO books (title, count_page, price, auth_id)
        VALUES ('мир', 806, 780.00, 25); """)


# CREATE TABLE books(
#         Id INTEGER PRIMARY KEY,
#         title TEXT NOT NULL,
#         count_page INTEGER NOT NULL CHECK (count_page >0),
#         price REAL CHECK (price >0),
#         auth_id INTEGER NOT NULL,
#         FOREIGN KEY (auth_id) REFERENCES auth(id)
#
# CREATE TABLE auth(
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         age INTEGER  CHECK (age >16)


# test_dict = {
#     'name': "Andrue", 'country': "Austria",
#     'personal_info': {'age': '27', 'sex': 'male'},
# }
#
# st = True
#
# while st:
#     print(f'STARTED {timet()}')
#     count = 0
#     for k, v in test_dict.items():
#         count += 1
#         print(f'|{k}: {v}')
#         if k == 'personal_info':
#             print(f'|{k}: {[items for items in v.items()]}')
#             print(count)
#             st = False
#             print(f'FINISH {timet()}')
#         else:
#             st = False
#             print("ELSE")


# import socket
#
# skt = socket.create_connection(("127.0.0.1", 10001))
#
#
# def mes(message: str):
#     m = bytes(message, 'utf8')
#     return skt.sendall(m)







