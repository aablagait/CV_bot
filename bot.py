import telegram
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import ReplyKeyboardMarkup

from views import my_git_hub, my_leetcode

# Записать токен и айди при запуске
TELEGRAM_TOKEN = 'token'
TELEGRAM_CHAT_ID = 'id'


bot = telegram.Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN)

def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([
        ['Аккаунт GitHub', 'Аккаунт LeetCode'],
    ])

    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}.\n Cпасибо, что посетили мой бот для поиска работы',
        reply_markup=buttons
    )


def text_message(update, context):
    chat = update.effective_chat
    message = update.message.text
    if message == 'Аккаунт GitHub':
        my_git_hub(chat, context)
    elif message == 'Аккаунт LeetCode':
        my_leetcode(chat, context)
    else:
        text = 'Ничего не понял, но очень интересно'
        context.bot.send_message(chat_id=chat.id, text=text)


# сделать кнопку /help
updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, text_message))


updater.start_polling()
updater.idle()