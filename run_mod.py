''' Import line '''

import asyncio
import os
import sys
import datetime
import time
from model.connect import migrate
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
                pass
            if message == '/get_info':
                stop_word2 = True
                while stop_word2:
                    for line2 in sys.stdin:
                        message = asyncio.run(parse_message(line2))
                        if message == '/get_txs':
                            print('YOUR LAST txs is ....')
                        if message == '/quit':
                            stop_word2 = False
                            print('You in menu')
                            break

            if message == '/run_db':
                print(migrate())
                print('Init databases')
            if message == '/stop':
                print('\nStoped process successfully!')
                stop_word = False
                break

