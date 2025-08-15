# edu_bot.py
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# --- CONFIG ---
BOT_TOKEN = "8399076842:AAFQ3M5gj4TmD9ZaeyIfqP9lWcxJPYl6fVo"
ADMIN_CHAT_ID = 6872304983

# --- LOGGING ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# --- DATA ---
grades = {
    "Grade 9": [
        {"question": "What is 2 + 3?", "answer": "5"},
        {"question": "What is the square of 4?", "answer": "16"},
        # Add 8 more questions...
    ],
    "Grade 10": [
        {"question": "Solve x in 2x + 3 = 7", "answer": "2"},
        {"question": "What is the area of a circle with radius 3?", "answer": "28.27"},
        # Add 8 more questions...
    ],
    "Grade 11": [
        {"question": "Derivative of x^2?", "answer": "2x"},
        {"question": "Integrate 2x dx?", "answer": "x^2 + C"},
        # Add 8 more questions...
    ],
    "Grade 12": [
        {"question": "Limit of (1 + 1/n)^n as n->∞?", "answer": "e"},
        {"question": "Solve 3x^2 - 12 = 0", "answer": "x=2 or x=-2"},
        # Add 8 more questions...
    ]
}

# --- COMMAND HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Grade 9", callback_data="Grade 9")],
        [InlineKeyboardButton("Grade 10", callback_data="Grade 10")],
        [InlineKeyboardButton("Grade 11", callback_data="Grade 11")],
        [InlineKeyboardButton("Grade 12", callback_data="Grade 12")],
        [InlineKeyboardButton("Support", callback_data="Support")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to Edu_pia Bot! Choose your grade to start learning:", reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    choice = query.data

    if choice in grades:
        # Send first question for selected grade
        question = grades[choice][0]["question"]
        await query.message.reply_text(f"{choice} STEM Question:\n\n{question}")
    elif choice == "Support":
        await query.message.reply_text(f"For support, contact the admin: @{ADMIN_CHAT_ID}")

# --- MAIN ---
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()
