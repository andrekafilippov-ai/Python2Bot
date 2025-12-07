from telebot import TeleBot, types

BOTTOKEN = "7750621677:AAHobAM7KCs0SUkqVfglEsZMV6u4BXNQtyA"

bot = TeleBot(BOTTOKEN) #связь с ботом



@bot.message_handler(commands=['photo'])
def sf(m):
    photo = open("hqdefault.jpg", "rb") #извлекаем картинку
    bot.send_photo(m.chat.id, photo) #отправялем в чат картинку
    bot.send_message(m.chat.id, "Цена: 1000 руб")
    bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAEPeJdo2qHhu_I4sZTH2tzDHWl6pS4p2AACo3wAAov1OUuFmVqEvYjDBTYE")

@bot.message_handler(commands=['start'])
def sf(m):
    bot.send_message(m.chat.id, "Helloy")


bot.infinity_polling()