import sqlite3
import datetime
import asyncio

URL_DB = '../../mydata.db'

time = datetime.datetime.now()
time_str = time.strftime('%Y-%m-%d %H:%m:%S')

connect = sqlite3.connect('D:\projects\microservice\mydata.db')
# // USE const 'FK_TRUE' for activate Foreign Keys in your db every time you call functions
# // FK_TRUE = connect.execute("PRAGMA foreign_keys = true")


def timet():
    now = datetime.datetime.now()
    now_str = now.strftime('%H:%M:%S')
    return now_str


""" INIT DATABASES """


def init_database():
    with connect as db:
        cursor = db.cursor()
        cursor.execute(""" CREATE TABLE users_bit(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        account TEXT NOT NULL,
        Date DATATIME NOT NULL
        )""")
        db.commit()


def second_database():
    with connect as db:
        cursor = db.cursor()
        cursor.execute(""" CREATE TABLE transactions(
        id INTEGER PRIMARY KEY,
        account TEXT NOT NULL,
        balance TEXT NOT NULL,
        transactions TEXT NOT NULL,
        Date DATATIME NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users_bit(id)
        )""" )
        db.commit()


""" MODELS """


class UserModel:
    """ Funny ORM commands """

    async def create_user(self, name, email, account):
        if await user_exist(mail=email) is not None:
            return 'User with email already exist'
        else:
            with connect as db:
                user_date = (name, email, account, time_str)
                cursor = db.cursor()
                cursor.execute("""INSERT INTO users_bit (name, email, account,Date) VALUES(?,?,?,?); """, user_date)
                db.commit()
                return 'Success!'

    async def update_user(self, name, email):
        #TODO в разработке
        pass

    async def delete_user(self, name, email, account):
        with connect as db:
            cursor = db.cursor()
            cursor.execute(f""" DELETE FROM users_bits WHERE name = '{name}' AND email = '{email}' AND account = '{account}' """)
            db.commit()
            return "Successfully deleted "

    @staticmethod
    async def get_user_info(name, email):
        with connect as db:
            query = db.execute(f""" SELECT id,name,email,account FROM users_bit WHERE name == '{name}' AND email == '{email}' """)
            result = query.fetchall()
            db.commit()
            if result == []:
                return 'Введите правильно данные или же данные отсутствуют'
            else:
                return result[0]


class TransactionsModel:
    """ NOT FUNNY ORM commands"""

    async def create_trns(self, account, balance, transactions, users_id):
        try:
            if await tnx_exist(tnx=transactions) is None:
                with connect as db:
                    connect.execute("PRAGMA foreign_keys = true") # PRAGMA идет передача аргумента, дабы не настраивать в ручну отношение FK
                    transactions_date = (account, balance, transactions, time_str, users_id)
                    cursor = db.cursor()

                    cursor.execute(f""" INSERT INTO transactions (account, balance, transactions, Date, user_id) VALUES(?,?,?,?,?); """, transactions_date)
                    db.commit()
                    return 'OK'
            else:
                return 'Transactions is exist in table'
        except sqlite3.IntegrityError:
            return 'ERROR: FOREIGN KEY constraint failed !!!'

    async def update_trns(self):
        pass

    async def delete_trns(self, account):
        with connect as db:
            # TODO добавить каскадное удаление или удаление последней транкзы
            cursor = db.cursor()

            cursor.execute(f""" DELETE FROM transactions WHERE account = '{account}' """)

            db.commit()
            return 'Successfully deleted!'

    @staticmethod
    async def get_trns_info(account, user_id):
        with connect as db:
            cursor = db.cursor()

            query_list = cursor.execute(
                f""" SELECT transactions,balance FROM transactions 
                WHERE user_id = '{user_id}' AND account = '{account}' """)

            result = query_list.fetchall()
            return result


async def user_exist(mail):
    with connect as db:
        query_set = db.execute(f""" SELECT email FROM users_bit WHERE email == '{mail}' """)
        result = query_set.fetchone()
        return result


async def tnx_exist(tnx):
    with connect as db:
        query_set = db.execute(f""" SELECT transactions FROM transactions WHERE transactions == '{tnx}' """)
        result = query_set.fetchone()
        return result


def migrate():
    """ FAKE MIGRATIONS """
    try:
        init_database()
        second_database()
        connect.close()
        return 'Succefull migrations'
    except sqlite3.OperationalError:
        return 'ERROR: Tables already exists'


""" TEST CONTROLLERS """


async def main(*args):
    print(*args)
    user_c = UserModel()
    txr_m = TransactionsModel()
    # task2 = asyncio.create_task(txr_m.create_trns(
    #     account='2x0924s15112512b',
    #     balance='500',
    #     transactions='4x4b3e759bf4e3e47e27213c0e7709c470043f514d2a2cbb22f555540c5819fdc7',
    #     users_id=6))
    task1 = asyncio.create_task(user_c.create_user(*args))
    print(f'RES-1 answerd {timet()}')
    res1 = await asyncio.gather(task1)
    # res2 = await asyncio.gather(task2)
    task3 = asyncio.create_task(user_c.get_user_info(name='Test1', email='test1@mail.ru'))
    res3 = await asyncio.gather(task3)
    print(res3[0][0])
    print('_________________________________________________')
    return res3

if __name__ == '__main__':
    print(f'STARTED {timet()}')
    ioloop = asyncio.get_event_loop()
    ss = ioloop.run_until_complete(main('Test3', 'test3@mail.ru', '3x0924s15112512b'))
    print(ss)
    print(f'FINISHED {timet()}')
    ioloop.close()