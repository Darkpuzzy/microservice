import asyncio
from model.models import Users, Transaction
from service.bitservice.bitfunc import *
from bit.network import NetworkAPI, satoshi_to_currency

# TODO довести вызовы к бд до одной строчки! Постараться сделать чистый код


class Get:

    @classmethod
    async def txs(cls, account, name, email, value: str):
        tnx = await BitFunc.get_txn(name=name, email=email)
        balance = await BitFunc.get_balance(name=name, email=email, value=value)
        await cls.__update_models(account=account, balance=balance, tnx=tnx, name=name, email=email)
        return f'Last transactions: {tnx}\n Your balance: {balance}'

    @classmethod
    async def user_info(cls, name, email, account):
        """ Запрос на полную информацию юзера будет происходить через адресс и мыло """
        user_info = await Transaction.full_info(name=name, email=email, account=account)
        return user_info
    """ Приватный метод обновления при вызове def txs """

    @classmethod
    async def __update_models(cls, account, balance, tnx, name, email):
        update = await Transaction._create_trn(account=account, balance=balance, trnx=tnx, name=name, email=email)
        return update


class Register:

    @classmethod
    async def reg(cls, name, email, account):
        f = await Users.create_profile(name=name, email=email, account=account)
        return f