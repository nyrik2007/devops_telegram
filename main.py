import telebot

bot = telebot.TeleBot("5850944713:AAFbvk5w2HD7lah73BS0ru1IJ5G-q2jS5xA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, "Bot by Nurbolat Konakbayev")

bot.infinity_polling()
