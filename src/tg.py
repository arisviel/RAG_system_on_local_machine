from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackContext,
)
import requests


async def q(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.text)
    await update.message.reply_text(update.message.text[7:])


async def echo(update: Update, context: CallbackContext) -> None:
    response = requests.get("http://127.0.1.1:5000/users")
    if response.status_code == 200:
        data = response.json()
    await update.message.reply_text(f"Лул")


with open("./data/token.txt", "r") as t:
    token = t.read()

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("q_rag", q))

app.run_polling()
