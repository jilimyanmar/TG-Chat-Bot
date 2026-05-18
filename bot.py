from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters
)

TOKEN = "8963669087:AAGkuscOJKM4XF6uNuJ5HU_-ikWvLa7IvyY"

# -------- MENU BUTTON --------
menu = ReplyKeyboardMarkup(
    [["hi", "price"], ["help", "menu"]],
    resize_keyboard=True
)

# -------- /start --------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bot စတင်ပါပြီ 👋\nMenu ကိုသုံးပါ",
        reply_markup=menu
    )

# -------- MESSAGE HANDLER --------
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.lower().strip()

    # 🔥 DEBUG (အရေးကြီး)
    print("USER MESSAGE:", text)

    responses = {
        "hi": "မင်္ဂလာပါ 👋",
        "hello": "Hello 👋",
        "price": "Price - 5000 MMK 💰",
        "help": "Hi / Price / Menu ကိုသုံးနိုင်ပါတယ်",
        "menu": "Menu ကိုအောက်မှာကြည့်ပါ 👇"
    }

    for key in responses:
        if key in text:
            await update.message.reply_text(responses[key], reply_markup=menu)
            return

    await update.message.reply_text("မသိတဲ့စာပါ 😅", reply_markup=menu)


# -------- APP --------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
