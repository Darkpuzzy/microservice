""" Import line """

import asyncio
import os
import sys
from service.views import Get, Register
from model.connect import migrate
from bit.network import NetworkAPI, satoshi_to_currency

''' PARSE FUNCTION '''


async def parse_message(message: str):
    pars_mode = message.replace("\n", "")
    return pars_mode

''' STARTED LOCAL PROGRAM '''
# запуск клиента в доработке

if __name__ == "__main__":
    stop_word = True
    print('\nHello, this microservice is for tracking crypto transaction and wallet ')
    print('The first step is registration your wallet and user info\nEnter /reg and /help for more info\n')

    while stop_word:
        for line in sys.stdin:  # sys.stdin ожидающий цикл для принятия сообщений, активится в момент поступления
            message = asyncio.run(parse_message(line))
            if message == '/help':
                print('\n| INFO FOR COMANDLINE |\n\n -/help - more info\n -/stop - stopped process\n -/run_db - init database\n')
            if message == '/reg':
                stop = True
                while stop:
                    n = str(input('Enter name: '))  #TODO позже опрокинуть в отдельную функцию
                    e = str(input('Enter email: '))
                    a = str(input('Enter account(address): '))
                    reg = asyncio.run(Register.reg(name=n, email=e, account=a))
                    print(reg)
                    print(f'Succes Name: {n} | Email: {e} | Account: {a}\n')
                    stop = False
            if message == '/get_info':
                stop_word2 = True
                while stop_word2:
                    for line2 in sys.stdin:
                        message2 = asyncio.run(parse_message(line2))
                        if message2 == '/get_txs':
                            while True:
                                n = str(input('Enter name: '))
                                e = str(input('Enter email: '))
                                a = str(input('Enter account(address): '))
                                v = str(input('Enter value (UST, BTC, ETC): '))
                                result = asyncio.run(Get.txs(account=a, name=n, email=e, value=v))
                                print(f'{result}\n')
                                break
                        if message2 == '/get_user':
                            n = str(input('Enter name: '))
                            e = str(input('Enter email: '))
                            a = str(input('Enter account(address): '))
                            user_info = asyncio.run(Get.user_info(name=n, email=e, account=a))
                            print(f'{user_info}\n')
                        if message2 == '/quit':
                            stop_word2 = False
                            print('You in menu\n')
                            break

            if message == '/run_db':
                print(migrate())
                print('Init databases\n')
            if message == '/stop':
                print('\nStoped process successfully!')
                stop_word = False
                break

