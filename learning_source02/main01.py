import os
from telegram import Bot
from telegram.ext import (
    Updater, CallbackContext, CommandHandler
)
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("token")
bot = Bot(token=token)
print(bot.get_me())

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher


def start(updater: Updater, context: CallbackContext):
    print('User input "/start"')
    bot.send_message(
        chat_id=updater.effective_chat.id,
        text="asdf~~"
    )

start_handler = CommandHandler("start", start)

print('start')
dispatcher.add_handler(start_handler)

updater.start_polling()