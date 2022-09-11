''' Import line '''

import asyncio
import os
import sys
import datetime
import time

''' PARSE FUNCTION '''


async def parse_message(message: str):
    pars_mode = message.replace("\n","")
    return pars_mode

''' STARTED LOCAL PROGRAM '''

if __name__ == "__main__":
    stop_word = True
    print('Hello, this microservice is for tracking crypto transaction and wallet ')
    print('The first step is registration your wallet and user info\nEnter /reg and /help for more info\n')

    while stop_word:
        for line in sys.stdin:
            message = asyncio.run(parse_message(line))
            if message == '/help':
                print('\n| INFO FOR COMANDLINE |\n\n -/help - more info\n -/stop - stopped process\n')
            if message == '/reg':
                pass
            if message == '/stop':
                print('\nStoped process successfully!')
                stop_word = False
                break
