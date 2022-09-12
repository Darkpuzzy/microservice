from bit.network import NetworkAPI, satoshi_to_currency
from model.connect import full_info
import json
import asyncio
from model import models


""" ЗАБИРАЕМ ДАННЫЕ ИЗ БИРЖИ И ОТРПАВЛЯЕМ В БД И ЗАПИСЫВАЕМ ДАННЫЕ """
""" Идет запрос к данным из файла, функции получают нужные штуки и передают в функции БД, далее эти аргументы отдаем пользователю через интерфейс"""

class BitFunc:

    @classmethod
    async def __get_adress(cls, name, email):
        Users = models.Users
        get_adress = await asyncio.gather(
            asyncio.create_task(
                Users.get_model(
                    name=name,
                    email=email)
            )
        )
        return get_adress[0][-1]

    @classmethod
    async def get_info(cls, email=None):
        if email == None:
            return 'Please enter address wallet'
        else:
            # TODO запрос на информацию кошелек и баланс
            pass

    @classmethod
    async def get_balance(cls, name, email, value: str):
        address = await cls.__get_adress(name=name, email=email)
        balanced = satoshi_to_currency(NetworkAPI.get_balance(address=address), value)
        return f'Your balance: {balanced} {value}'

    @classmethod
    async def get_txn(cls, name, email):
        address = await cls.__get_adress(name=name, email=email)
        txn = NetworkAPI.get_transactions(address)

""" ПРИМЕР И ОБРАЗЕЦ """

# address = '35PqpdHUQuURn9LdFyTNDLYkdkWM3w36PG' bc1qw8wrek2m7nlqldll66ajnwr9mh64syvkt67zlu

# Искать кошельки с транзакциями не больше 10 штук

address = '35PqpdHUQuURn9LdFyTNDLYkdkWM3w36PG'

# TODO получение баланса
s = satoshi_to_currency(NetworkAPI.get_balance(address), 'usd')
print(s + ' usd')
print(type(s))

# TODO получение остатка с транзакции
j = NetworkAPI.get_unspent(address)
print(j)

# TODO получение хэшэй транзакций
f = NetworkAPI.get_transactions(address)
print(f)


""" TEST POINT """

if __name__ == '__main__':
    f = asyncio.run(BitFunc._get_adress(name='Test4',email='test4@mail.ru'))
    print(f)