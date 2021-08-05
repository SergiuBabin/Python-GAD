import logging

from aiogram import Bot, Dispatcher, executor, types

import db
import exceptions
import expense
from categories import Categories

API_TOKEN = '1914713245:AAHk7hf5Xl7_RkgoJAWwAfSikwsWYASG__U'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    Send welcome message and boot command help.
    """
    if len([item for item in db.fetchall('user_info', 'id name'.split()) if message.from_user.id == item['id']]) == 0:
        db.insert("user_info", {
            "id": message.from_user.id,
            "name": message.from_user.first_name,
        })

    await message.reply(
        f"Hi {message.from_user.first_name}!\nI'm Expenditure Bot!\n\n"
        "Add expense: 50 food\n"
        "Today's statistics: /today\n"
        "For the current month: /month\n"
        "Last entered expenses: /expenses\n"
        "Spend categories: /categories")

@dp.message_handler(commands=['categories'])
async def categories_list(message: types.Message):
    """Get all categories"""
    categories = Categories().get_all_categories()
    answer_message = "Expense Category:\n\n* /" + \
                     ("\n* /".join([c.name + ' (' + ", ".join(c.aliases) + ')' for c in categories]))
    await message.reply(answer_message)


@dp.message_handler(commands=list(c.name for c in Categories().get_all_categories()))
async def categories_list(message: types.Message):
    """Get all categories"""
    answer_message = expense.get_category_statistics(message.from_user.id, message.text[1:])
    await message.reply(answer_message)


# @dp.message_handler(commands=[])
# async def categories_list(message: types.Message):
#     """Get all categories"""
#     categories = Categories().get_all_categories()
#     answer_message = "Expense Category:\n\n* /" + \
#                      ("\n* /".join([c.name + ' (' + ", ".join(c.aliases) + ')' for c in categories]))
#     await message.reply(answer_message)

# @dp.message_handler(commands=['date'])
# async def date_expenses(message: types.Message):
#     """Get all date's expenses"""
#     try:
#         answer_message = expense.get_date_statistics(message.from_user.id, message.text)
#     except exceptions.NotCorrectMessage as e:
#         await message.reply(str(e))
#         return
#
#     await message.reply(answer_message)

@dp.message_handler(commands=['today'])
async def today_expenses(message: types.Message):
    """Get all today's expenses"""
    answer_message = expense.get_today_statistics(message.from_user.id)
    await message.reply(answer_message)


@dp.message_handler(commands=['month'])
async def month_expenses(message: types.Message):
    """Get all month's expenses"""
    answer_message = expense.get_month_statistics(message.from_user.id)
    await message.reply(answer_message)


@dp.message_handler(commands=['expenses'])
async def last_expenses(message: types.Message):
    """Get last expenses"""
    last_expense = expense.last(message.from_user.id)
    answer_message = f"Last {len(last_expense)} expenses: \n\n" + \
                     ("\n".join(str(e.amount) + ' ' + e.category_name for e in last_expense))
    await message.reply(answer_message)

@dp.message_handler()
async def add_expense(message: types.Message):
    """Add new expense"""
    try:
        expens = expense.add_expense(message.text, message.from_user.id)
    except exceptions.NotCorrectMessage as e:
        await message.reply(str(e))
        return

    answer_message = (
        f"Added spending  {expens.amount} RON on {expens.category_name}.\n\n"
        f"{expense.get_today_statistics(message.from_user.id)}")
    db.get_table("expense")
    await message.reply(answer_message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)