import os
import logging

import telegram
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import ReplyKeyboardMarkup
from dotenv import load_dotenv

from views import TextMessage, CommandMessage


logging.basicConfig(
    format='%(asctime)s - '
           '%(levelname)s - '
           '%(funcName)s - '
           '%(lineno)s - '
           '%(message)s',
    level=logging.INFO,
    filename='logs/main.log',
    filemode='w',
)

load_dotenv()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


bot = telegram.Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN)


def command_message(update, context):
    message = update.message.text
    if message == '/start':
        return CommandMessage(update, context).start()
    if message == '/help':
        return CommandMessage(update, context).help()


def text_message(update, context):
    chat = update.effective_chat
    message = update.message.text
    name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    logging.info(f'Пользователь {name} {last_name} отправил сообщение - "{message}"')
    if message == 'Аккаунт GitHub':
        return TextMessage(chat, context).my_git_hub()
    elif message == 'Аккаунт LeetCode':
        return TextMessage(chat, context).my_leet_code()
    elif message == 'Резюмэ на HH.ru':
        return TextMessage(chat, context).my_hh()
    elif message == 'Мой телеграмм':
        return TextMessage(chat, context).my_tg()
    else:
        return TextMessage(chat, context).dont_understand()


logging.info('Бот в работе!')
updater.dispatcher.add_handler(CommandHandler('start', command_message))
updater.dispatcher.add_handler(CommandHandler('help', command_message))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text_message))


updater.start_polling()
updater.idle()

logging.info('Бот выключен!')
