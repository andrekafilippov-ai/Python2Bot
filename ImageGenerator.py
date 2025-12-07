from telebot import TeleBot
import random
import requests

BOTTOKEN = "8484808241:AAHXxf829o5HaPe35rHOr3Y9CnjM513VUl4"
bot = TeleBot(BOTTOKEN)

@bot.message_handler(commands=['img'])
def sendImg(m):
    bot.reply_to(m, "Генерирую")
    prompt = m.text.partition(' ')[2].strip()
    seed = random.randint(0, 2_000_000_000)
    url = f"https://image.pollinations.ai/prompt/{prompt}?width=768&height=768&seed={seed}&n=1"
    r = requests.get(url, timeout=90, allow_redirects=True)
    bot.send_photo(m.chat.id, r.content, caption="Готово ✅")


bot.infinity_polling()