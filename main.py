from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3 as sql3
from config import TOKEN
# from db_manage import sign_up_db
from db_manage import User, DataBase
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

conn = sql3.connect('OOPmain.db')
c = conn.cursor()


# Handler for start bot
@dp.message_handler(commands='start')
async def start_bot(msg: types.Message):
    await msg.answer('Hello, click to sign up --- /reg')

@dp.message_handler(commands='reg')
async def sign_up(msg: types.Message):
    info = msg
    username = info.chat.username
    user_id = info.chat.id
    us = User(username, user_id)
    db = DataBase('OOPmain.db')
    us.load_into_db(db)
    # sign_up_db(username, user_id)
    await msg.answer('You signed up successfully!')


if __name__ == '__main__':
    executor.start_polling(dp)