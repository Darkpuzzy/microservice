import asyncio
# TODO довести вызовы к бд до одной строчки! Постараться сделать чистый код


class Get:

    @classmethod
    async def txs(cls):
        pass

    @classmethod
    async def user_info(cls):
        """ Запрос на полную информацию юзера будет происходить через адресс и мыло """
        pass

    """ Приватный метод обновления при вызове def txs """

    @classmethod
    async def __update_models(cls):
        pass


class Register:

    @classmethod
    async def reg(cls, name, email, account):
        pass
