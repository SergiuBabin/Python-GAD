from typing import NamedTuple, Optional

import datetime
import pytz
import re

import db
import exceptions
from categories import Categories

class Message(NamedTuple):
    amount: int
    category_text: str

class Expense(NamedTuple):
    id: Optional[int]
    amount: int
    category_name: str

def add_expense(raw_message: str, user_id: int) -> Expense:
    parsed_message = _parse_message(raw_message)
    category = Categories().get_category(
        parsed_message.category_text)
    db.insert("expense", {
        "amount": parsed_message.amount,
        "user_id": user_id,
        "created": _get_now_formatted(),
        "category": category.name,
        "note": raw_message
    })
    return Expense(id=None,
                   amount=parsed_message.amount,
                   category_name=category.name)

def get_category_statistics(id_user: int, categ: str) -> str:
    cursor = db.get_cursor()
    cursor.execute("select sum(amount) "
                   f"from expense where user_id = {id_user} and category = '{categ}'")
    result = cursor.fetchone()
    if not result[0]:
        return f"No expenses for {categ}"

    return (f"All time expenses for {categ} :\n"
            f"Total — {result[0]} RON.\n")


def get_today_statistics(id_user: int) -> str:
    cursor = db.get_cursor()
    cursor.execute("select sum(amount) "
                   "from expense where date(created)=date('now', 'localtime') "
                   f"and user_id = {id_user}")
    result = cursor.fetchone()
    if not result[0]:
        return "No expenses today"
    all_today_expenses = result[0]
    cursor.execute("select sum(amount)"
                   "from expense where date(created)=date('now', 'localtime') "
                   "and category in (select name "
                   "from category where is_base_expense=true)"
                   f"and user_id = {id_user}")
    result = cursor.fetchone()
    base_today_expenses = result[0] if result[0] else 0

    cursor.execute("select category, sum(amount) "
                   f"from expense where date(created)=date('now', 'localtime')  and user_id = {id_user} "
                   "group by category "
                   "order by 2 desc")
    result = cursor.fetchall()
    return (f"Expenses today:\n"
            f"Total — {all_today_expenses} RON.\n"
            f"Basic — {base_today_expenses} RON. from {_get_budget_limit()} RON.\n\n"
            "For the current month: /month\n\n"
            "Detailed:\n"
            + ("\n".join(str(text).capitalize() + ' - ' + str(res) for text, res in result)))

def get_month_statistics(id_user: int) -> str:
    cursor = db.get_cursor()
    cursor.execute("select sum(amount) "
                   "from expense where strftime('%Y',date(created)) = strftime('%Y',date('now', 'localtime')) "
                   "and strftime('%m',date(created)) = strftime('%m',date('now', 'localtime'))"
                   f" and user_id = {id_user}")
    result = cursor.fetchone()
    if not result[0]:
        return "No expenses this month"
    all_today_expenses = result[0]
    cursor.execute("select sum(amount)"
                   "from expense where strftime('%Y',date(created)) = strftime('%Y',date('now', 'localtime'))"
                   "and strftime('%m',date(created)) = strftime('%m',date('now', 'localtime'))"
                   "and category in (select name "
                   "from category where is_base_expense=true)"
                   f"and user_id = {id_user}")
    result = cursor.fetchone()
    base_today_expenses = result[0] if result[0] else 0

    cursor.execute("select category, sum(amount) "
                   "from expense where strftime('%Y',date(created)) = strftime('%Y',date('now', 'localtime')) "
                   "and strftime('%m',date(created)) = strftime('%m',date('now', 'localtime'))"
                   f" and user_id = {id_user} "
                   "group by category "
                   "order by 2 desc")
    result = cursor.fetchall()
    return (f"Expenses this month:\n"
            f"Total — {all_today_expenses} RON.\n"
            f"Basic — {base_today_expenses} RON. from {_get_budget_limit()} RON.\n\n"
            "Detailed:\n"
            + ("\n".join(str(text).capitalize() + ' - ' + str(res) for text, res in result)))


# def get_date_statistics(id_user: int, date: str) -> str:
#     regexp_result = re.search('/date(.+?)', date)
#
#     if not regexp_result.group(1):
#         raise exceptions.NotCorrectMessage(
#             "Can't understand the message. Write a message in the format, "
#             "like:\n/date Day.Month.Year(24.05.2021)")
#
#     cursor = db.get_cursor()
#     return


def last(id_user: int) -> str:
    cursor = db.get_cursor()
    cursor.execute(
        "select ex.id, ex.amount, c.name "
        "from expense ex left join category c "
        "on c.name = ex.category "
        f"where user_id = {id_user} "
        "order by created desc limit 3")

    rows = cursor.fetchall()
    last_expenses = [Expense(id=row[0], amount=row[1], category_name=row[2]) for row in rows]
    return last_expenses

def plot_expenses(id_user: int) -> str:
    cursor = db.get_cursor()
    cursor.execute("select sum(amount) "
                   "from expense where strftime('%Y',date(created)) = strftime('%Y',date('now', 'localtime')) "
                   "and strftime('%m',date(created)) = strftime('%m',date('now', 'localtime'))"
                   f" and user_id = {id_user}")
    result = cursor.fetchone()
    if not result[0]:
        return "No expenses this month"
    pass

def _get_budget_limit() -> str:
    return '500'

def _parse_message(raw_message: str) -> Message:
    regexp_result = re.match(r"([\d ]+) (.*)", raw_message)

    if not regexp_result.group(0) or not regexp_result.group(1) \
            or not regexp_result.group(2):
        raise exceptions.NotCorrectMessage(
            "Can't understand the message. Write a message in the format, "
            "like:\n1500 coffee")

    amount = regexp_result.group(1).replace(" ", "")
    category_text = regexp_result.group(2).strip().lower()
    return Message(amount=amount, category_text=category_text)

def _get_now_formatted() -> str:
    return _get_now_datetime().strftime("%Y-%m-%d %H:%M:%S")

def _get_now_datetime() -> datetime.datetime:
    tz = pytz.timezone("Europe/Bucharest")
    now = datetime.datetime.now(tz)
    return now