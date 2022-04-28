import logging
import html
import json
import logging
import traceback
import os

from telegram import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo, Update
from telegram.ext import (
    CommandHandler,
    Application,
    CallbackContext,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [KeyboardButton("Выбрать торт", web_app=WebAppInfo(url='https://egorikas.com/cake-store.github.io'))],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    msg = """
*Давайте сделаем заказ* 🍰
    
Нажмите на кнопку, чтобы выбрать свой торт\!
"""
    await update.message.reply_markdown_v2(text=msg, reply_markup=reply_markup)

# 'web_app_data': {'data': '[{"id":1,"count":2,"price":764}]'

async def help_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Вызовите /start чтобы заказать торт.")

async def echo(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    if update.effective_message.web_app_data is None:
        return

    body = ""
    data = json.loads(update.effective_message.web_app_data.data)
    for i in data:
        temp = f'{i["title"]} {i["count"]} шт - {i["count"] * i["price"]} ₽ \n'
        body += temp

    msg = f"""Спасибо за заказ {update.effective_message.from_user.name}! 🍰

*Ваш заказ*:
{body}
В ближайшее время с Вами свяжутся!

Хорошего дня!
"""

    
    """Echo the user message."""
    await update.message.reply_markdown(text=msg)


async def error_handler(update: object, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    logger.error(msg="Exception while handling an update:", exc_info=context.error)


def main() -> None:
    # """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(os.getenv('BOTAPIKEY')).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.ALL, echo))
    application.add_error_handler(error_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()



if __name__ == '__main__':
    main()