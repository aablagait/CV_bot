from telegram import ReplyKeyboardMarkup


ACCOUNT_GIT_HUB = 'https://github.com/aablagait'
ACCOUNT_LEET_CODE = 'https://leetcode.com/u/aablagait/'
ACCOUNT_HEAD_HUNTER = ('https://hh.ru/resume/'
                       '4a413b7aff08b29e280039ed1f365658704f75')
IMAGE_QR_QODE_TG = 'images/qc_tg.jpg'


class TextMessage():
    def __init__(self, chat, context):
        self.chat= chat
        self.context = context

    def my_git_hub(self):
        return (self.context.bot
                .send_message(chat_id=self.chat.id,
                              text=ACCOUNT_GIT_HUB)
                )

    def my_leet_code(self):
        return (self.context.bot
                .send_message(chat_id=self.chat.id,
                              text=ACCOUNT_LEET_CODE)
                )

    def my_hh(self):
        return (self.context.bot
                .send_message(chat_id=self.chat.id,
                              text=ACCOUNT_HEAD_HUNTER)
                )

    def my_tg(self):
        return (self.context.bot
                .send_photo(chat_id=self.chat.id,
                            photo=open(IMAGE_QR_QODE_TG, "rb"))
                )

    def dont_understand(self):
        text = 'Ничего не понял, но очень интересно'
        return self.context.bot.send_message(chat_id=self.chat.id,
                                             text=text)


class CommandMessage():
    def __init__(self, update, context):
        self.update= update
        self.context = context

    def start(self):
        chat = self.update.effective_chat
        name = self.update.message.chat.first_name
        buttons = ReplyKeyboardMarkup([
            ['Аккаунт GitHub', 'Аккаунт LeetCode'],
            ['Резюмэ на HH.ru', 'Мой телеграмм']
        ])

        return self.context.bot.send_message(
            chat_id=chat.id,
            text=f'Привет, {name}.\n'
                 f'Cпасибо, что посетили мой бот для поиска работы',
            reply_markup=buttons
        )

    def help(self):
        chat = self.update.effective_chat
        name = self.update.message.chat.first_name
        message = (f'{name}, чем вам помочь?\n'
                   f'Ниже есть кнопки, нажав на которые\n '
                   f'откроются ссылки на мои аккаунты')

        return self.context.bot.send_message(
            chat_id=chat.id,
            text=message,
        )
