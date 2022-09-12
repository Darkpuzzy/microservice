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
    async def __get_user_id(cls, name, email):
        get_user_id = await asyncio.gather(
            asyncio.create_task(
               Users.get_model(
                   name=name,
                   email=email)
            )
        )
        result = get_user_id[0]
        return result[0]

    @classmethod
    async def _create_trn(cls, account, balance, trnx, name, email):
        user_id = await Transaction.__get_user_id(name=name, email=email)
        result = await asyncio.gather(
            asyncio.create_task(
                cls.model.create_trns(
                    account=account,
                    balance=balance,
                    transactions=trnx,
                    users_id=user_id
                )
            )
        )
        return result[0]

    @classmethod
    async def get_all_trn(cls, account, name, email):
        """ Taked all trn for user_id """
        user_id = await Transaction.__get_user_id(name=name, email=email)
        result = await cls.model.get_trns_info(account=account, user_id=user_id)
        return result

    @classmethod
    async def get_trn(cls, account):
        pass

# TODO User_id повторяется в моментах,
#  нужно подумать о том что бы вынести как
#  отдельную функцию вызова получения айдишника + распарсить


"""TEST POINT"""


async def main():
    task = asyncio.create_task(Users.create_profile(name='Test6', email='test6@mail.ru', account='6x0924s15112512b'))
    res = await asyncio.gather(task)
    task1 = asyncio.create_task(Users.get_model(name='Test4', email='test4@mail.ru'))
    res1 = await asyncio.gather(task1)
    task2 = asyncio.create_task(Transaction._create_trn(
        account='4x0924s15112512b',
        balance=320,
        trnx='6x4b3e759bf4e3e47e27213c0e7709c470043f514d2a2cbb22f555540c5819fdc7',
        name='Test7',
        email='test7@mail.ru'
    ))
    res2 = await asyncio.gather(task2)
    res3 = await Transaction.get_all_trn(account='2x0924s15112512b', name='Test2', email='test2@mail.ru')
    return res3[-1]


if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    ss = ioloop.run_until_complete(main())
    print(ss)
