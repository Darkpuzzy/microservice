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
        )""")
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
#
#
# def _razryad(b):
#     to_string = str(b)
#     list_numbers = []
#     string_numbers = ""
#     if to_string.isdigit():
#         mass_chsla = len(to_string) - 1
#         while mass_chsla > 0:
#             for item in to_string:
#                 print(item)
#                 list_numbers.append(f'{item}' + '_' * mass_chsla)
#                 mass_chsla -= 1
#         for n in list_numbers:
#             print(n)
#             string_numbers += n
#         return string_numbers
#     else:
#         return "ENTER THE ONLY NUMBERS"
#
# print(_razryad(b=123456))

# p = 5*216**1156-4*36**1147+6**1153-875
# k1 = 0 # количество нулей
# k2 = 0 # количество пятёрок
# a = 6
# while p>0:
#     c=p%a
#     if c==0:k1+=1
#     p//=a
#     print(p)
#     if c==5:k2+=1
# print(k1, k2)
# print(k2-k1)

# for x in range(10000):
#     p = 4**1014-2**x+12
#     print(x)
#     k=0
#     a=2
#     while p>0:
#         c=p%a
#         if c==0:
#             k+=1
#         p//=a
#     if k== 2000:
#         print(x)
#         break
