import os
import telebot
import requests

from dotenv import load_dotenv
from http import HTTPStatus

load_dotenv()

TOKEN: str = os.getenv('TOKEN')
API_TOKEN: str = os.getenv('API_user_token')

ENDPOINT: str = 'http://moneybox.ddns.net/api/v1/report/'
HEADERS: dict = {'Authorization': f'Token {API_TOKEN}'}


bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['report'])
def get_report(message):

    report = requests.get(ENDPOINT, headers=HEADERS)
    if report.status_code != HTTPStatus.OK:
        res = (f'Эндпоинт {ENDPOINT} недоступен. '
               f'Код ответа API: {report.status_code}')
        
    else:
        res = ''
        data = report.json()['report_data']
        for elem in data:
            res += f'{elem}: {str(data[elem])}\n'

    bot.send_message(message.chat.id, res)


bot.infinity_polling()