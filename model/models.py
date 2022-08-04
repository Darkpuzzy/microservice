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

    async def create_profile(self):
        result = await asyncio.gather(
            asyncio.create_task(
                self.model.create_user(
                    name=self.name, email=self.email, account=self.account
                )
            )
        )
        return result[0]

    async def _update_model(self):
        pass

    async def get_model(self):
        pass


class Transaction:
    """ Model transaction """
    def __init__(self, account, transaction, user_id):
        self.account = account
        self.transaction = transaction
        self.user_id = user_id

    async def update_trn(self):
        pass

    async def get_trn(self):
        pass


async def main():
    f = Users(name='Test4', email='test4@mail.ru', account='4x0924s15112512b')
    task = asyncio.create_task(f.create_profile())
    res = await asyncio.gather(task)
    return res[0]


if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    ss = ioloop.run_until_complete(main())
    print(ss)
