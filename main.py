import telebot

from http import HTTPStatus
from telebot import types

from config import TOKEN, initialize_reports_api


bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['report'])
def get_report(message):

    reports_api = initialize_reports_api()
    reports = reports_api.report_html_retrieve_with_http_info()
    if reports.status_code == 200:
        bot.send_message(message.chat.id, f'{reports.raw_data}')


if __name__ == '__main__':
    bot.polling(non_stop=True)
