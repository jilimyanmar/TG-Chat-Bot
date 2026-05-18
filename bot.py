from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8963669087:AAEBAXUFOOVdGWBdGhkyby6e5VADABYvMwM"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()

    if "hi" in text:
        await update.message.reply_text("မင်္ဂလာပါ 👋")

    elif "price" in text:
        await update.message.reply_text("Price - 5000 MMK")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
