import telebot
from datetime import datetime
from http import HTTPStatus
from telebot import types

from config import (TOKEN,
                    initialize_reports_api,
                    initialize_expenses_api,
                    initialize_incomes_api)

from openapi_client import ReportsApi
from openapi_client.models import Expense, Invite

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['expense'])
def get_expense(message):

    api_client = initialize_expenses_api()
    
    expense = api_client.expense_list_with_http_info()

    bot.send_message(message.chat.id, f'{expense.raw_data}')


@bot.message_handler(commands=['report'])
def get_report(message):

    api_client = initialize_reports_api()

    report = api_client.report_list_with_http_info()

    bot.send_message(message.chat.id, f'{report.raw_data}')


@bot.message_handler(commands=['income'])
def get_income(message):

    api_client = initialize_incomes_api()
    
    income = api_client.income_list_with_http_info()

    bot.send_message(message.chat.id, f'{income.raw_data}')


if __name__ == '__main__':
    bot.polling(non_stop=True)
