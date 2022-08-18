import sqlite3
import asyncio
from connect import *


class Users:
    """ Model User"""
    model = UserModel()

    def __init__(self, name, email, account):
        self.name = name
        self.account = account
        self.email = email

    @classmethod
    async def create_profile(cls, name, email, account):
        result = await asyncio.gather(
            asyncio.create_task(
                cls.model.create_user(
                    name=name, email=email, account=account
                )
            )
        )
        return result[0]

    async def _update_model(self):
        pass

    @classmethod
    async def get_model(cls, name, email):
        result = await asyncio.gather(
            asyncio.create_task(
                cls.model.get_user_info(name=name, email=email)
            )
        )
        return result[0]


class Transaction:
    """ Model transaction """
    model = TransactionsModel()
    User = Users

    def __init__(self, account, transaction, user_id):
        self.account = account
        self.transaction = transaction
        self.user_id = user_id

    async def update_trn(self):
        pass

    @classmethod
    async def _create_trn(cls, account, balance, trnx, name, email):
        user_id = await asyncio.gather(
            asyncio.create_task(
                Users.get_model(
                    name=name,
                    email=email)))
        result = await asyncio.gather(
            asyncio.create_task(
                cls.model.create_trns(
                    account=account,
                    balance=balance,
                    transactions=trnx,
                    users_id=user_id[0][0]
                )
            )
        )
        return result[0]

    async def get_trn(self):
        pass


async def main():
    task = asyncio.create_task(Users.create_profile(name='Test5', email='test5@mail.ru', account='5x0924s15112512b'))
    res = await asyncio.gather(task)
    task1 = asyncio.create_task(Users.get_model(name='Test4', email='test4@mail.ru'))
    res1 = await asyncio.gather(task1)
    task2 = asyncio.create_task(Transaction._create_trn(
        account='4x0924s15112512b',
        balance=320,
        trnx='6x4b3e759bf4e3e47e27213c0e7709c470043f514d2a2cbb22f555540c5819fdc7',
        name='Test4',
        email='test4@mail.ru'
    ))
    res2 = await asyncio.gather(task2)
    return res2


if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    ss = ioloop.run_until_complete(main())
    print(ss)
