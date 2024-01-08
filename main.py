import os
import telebot
import requests

from dotenv import load_dotenv
from http import HTTPStatus
from telebot import types

from openapi_client.api import reports_api

load_dotenv()

TOKEN: str = os.getenv('TOKEN')
API_TOKEN: str = os.getenv('API_TOKEN')

ENDPOINT: str = 'http://127.0.0.1:8000/api/v1/report/'
HEADERS: dict = {'Authorization': f'Token {API_TOKEN}'}


bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['report'])
def get_report(message):

    report = reports_api.Report
    

    # if report.status_code != HTTPStatus.OK:
    #     report_message = (f'Эндпоинт {ENDPOINT} недоступен. '
    #                       f'Код ответа API: {report.status_code}')
    #else:
    # report_message = ''
    # data = report.json().get('report_data')
    # for elem in data:
    #     report_message += f'{elem}: {str(data[elem])}\n'

    bot.send_message(message.chat.id, report)


if __name__ == '__main__':
    bot.polling(non_stop=True)
