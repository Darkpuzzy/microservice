from bit.network import NetworkAPI, satoshi_to_currency
from model.connect import full_info
import json


class BitFunc:

    async def get_info(self, email=None):
        if email == None:
            return 'Please enter address wallet'
        else:
            # TODO запрос на информацию кошелек и баланс
            pass

    async def get_full_info(self, email, address, name):
        pass

    async def get_balance(self, address, value: str):
        balanced = satoshi_to_currency(NetworkAPI.get_balance(address=address), value)
        return f'Your balance: {balanced} {value}'

    async def get_txn(self, address):
        txn = NetworkAPI.get_transactions(address)



# address = '35PqpdHUQuURn9LdFyTNDLYkdkWM3w36PG' bc1qw8wrek2m7nlqldll66ajnwr9mh64syvkt67zlu 35PqpdHUQuURn9LdFyTNDLYkdkWM3w36PG

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



