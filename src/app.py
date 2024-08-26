from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackContext,
)
from llm import gemma_handler

gemma = gemma_handler()

with open("./data/token.txt", "r") as t:
    token = t.read()


async def q(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(gemma.get_answer(update.message.text[3:]))


async def q_rag(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(gemma.get_answer_rag(update.message.text[5:]))


app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("q", q))

app.add_handler(CommandHandler("rag", q_rag))

app.run_polling()
