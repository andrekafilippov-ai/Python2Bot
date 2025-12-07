from telebot import TeleBot, types
from datetime import datetime
import threading
import time
import pandas

days_of_week = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}

BOTTOKEN = "8021856439:AAF4_5zZH5bBrL4Q6QhBPxrZSPKniq5_Y0U"

bot = TeleBot(BOTTOKEN) #связь с ботом

#список пользователей подпис. на уведом.
users = set()


@bot.message_handler(commands=['start'])
def sf(m):
    bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAEP2pdpIzM6S9PnGcMifhA6JQjq3AG7GgAC4QADNuwbBW5uM6aRdOCbNgQ")
    bot.send_message(m.chat.id, "Приветствую. Это бот Андрея Филиппова\n"
                                "Чтобы узнать, что делает бот, испльзуй команду /info")

@bot.message_handler(commands=['info'])
def info(m):
    Klava1 = types.InlineKeyboardMarkup()
    Klava2 = types.ReplyKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("/notice", callback_data="notice")
    btn2 = types.InlineKeyboardButton("/unsub", callback_data="unsub")
    btn3 = types.InlineKeyboardButton("/image", callback_data="image")
    btn4 = types.InlineKeyboardButton("/parser", callback_data="parser")

    btn5 = types.KeyboardButton("/notice")
    btn6 = types.KeyboardButton("/unsub")
    btn7 = types.KeyboardButton("/image")
    btn8 = types.KeyboardButton("/parser")

    Klava1.add(btn1, btn2, btn3, btn4)
    Klava2.add(btn5, btn6, btn7, btn8)

    bot.send_message(m.chat.id, "Список команд бота:\n"
                                "/start - приветсвтие\n"
                                "/info - все команды бота\n"
                                "/notice - подписаться на уведомления\n"
                                "/unsub - отписаться от уведомлений\n"
                                "/image - сгенерировать картинку по текстовому запросу\n"
                                "/parser - получить подборку товаров электроники по запросу", reply_markup=Klava1)

    bot.send_message(m.chat.id, "✅", reply_markup=Klava2)


def get_beautiful_column_name(column: str) -> str:
    """Преобразует названия колонок в красивые"""
    column_names = {
        'Time': '🕒 Время',
        'Subject': '📖 Предмет',
        'Teacher': '👨‍🏫 Преподаватель',
        'Room': '🏫 Аудитория',
    }
    return column_names.get(column, column)


@bot.message_handler(commands=['notice'])
def notice(m):
    users.add(m.chat.id)
    bot.send_message(m.chat.id, "✅ Вы подписались на уведомления")



@bot.message_handler(commands=['unsub'])
def notice(m):
    users.discard(m.chat.id)
    bot.send_message(m.chat.id, "❌ Вы отписались от уведомлений")


def setShedule(user):

    today_weekday = datetime.today().weekday() + 1


    # Суббота
    if today_weekday == 6:
        bot.send_message(
            user,
            "🎉 *Суббота* - занятий нет!\nМожно отдохнуть! 😊",
            parse_mode='Markdown'
        )
        return

    # Воскресенье
    if today_weekday == 7:
        bot.send_message(
            user,
            "🌟 *Воскресенье* - занятий нет!\nИдеальный день для отдыха! ☀️",
            parse_mode='Markdown'
        )
        return

    df = pandas.read_excel('Schedule.xlsx')

    today_schedule = df[df['Day'] == today_weekday]

    if today_schedule.empty:
        day_name = days_of_week.get(today_weekday, "сегодня")
        bot.send_message(
            user,
            f"🎉 *{day_name.upper()}* - занятий нет!\nОтличный день для саморазвития! 📚",
            parse_mode='Markdown'
        )
        return

    day_name = days_of_week.get(today_weekday, "сегодня")
    response = f"📚 *РАСПИСАНИЕ НА {day_name.upper()}* 📚\n\n"

    for _, row in today_schedule.iterrows():
        response += "▫️" * 20 + "\n"

    for column, value in row.items():
        if column != 'Day' and pandas.notna(value) and str(value).strip() != '':
            column_name = get_beautiful_column_name(column)
            response += f"*{column_name}:* {value}\n"

    response += "\n" + "═" * 30 + "\n\n"

    total_lessons = len(today_schedule)
    response += f"📊 *Всего пар: {total_lessons}*"

    bot.send_message(user, response, parse_mode='Markdown')

def check_time():
    while True:
        now = datetime.now()
        if now.hour == 20 and now.minute == 6:
            for user in list(users):
                setShedule(user)
        time.sleep(1)


def start_scheduler():
    scheduler_thread = threading.Thread(target=check_time)
    scheduler_thread.daemon = True  # фоновый поток
    scheduler_thread.start()



if __name__ == "__main__":
    print("Бот запущен...")
    start_scheduler()              # Запуск фоновых уведомлений
    bot.polling(none_stop=True)    # Основной цикл бота
































# from telebot import TeleBot, types
#
# BOTTOKEN = "7750621677:AAHobAM7KCs0SUkqVfglEsZMV6u4BXNQtyA"
#
# bot = TeleBot(BOTTOKEN) #связь с ботом
#
#
#
#
#
#
#
#
#
# bot.infinity_polling()
#
#




# @bot.message_handler(commands=['start'])
# def cmdStart(m):
#     kv = types.ReplyKeyboardMarkup()
#     kn = types.KeyboardButton("Привет")
#     kv.add(kn)
#     bot.send_message(m.chat.id, "выбери кнопку", reply_markup=kv)


# @bot.message_handler(commands=['start'])
# def start(message):
#     klava = types.InlineKeyboardMarkup() #Создать место под кнпки
#     Like = types.InlineKeyboardButton("Like", callback_data="Like") #создается кнопка со своим id
#     klava.add(Like) #соединяет клавиатуру и кнопку
#     bot.send_message(message.chat.id, "Нажми Like", reply_markup=klava)
#
# @bot.message_handler(commands=['info'])
# def cmdinfo(m):
#     klava = types.InlineKeyboardMarkup() #Создать место под кнпки
#     knopka = types.InlineKeyboardButton("Кнопка", callback_data="knopka") #создается кнопка со своим id
#     knopka1 = types.InlineKeyboardButton("Кнопка1", callback_data="knopka1")
#     klava.add(knopka) #соединяет клавиатуру и кнопку
#     klava.add(knopka1)
#     bot.send_message(m.chat.id, "Нажми кнопку", reply_markup=klava)
#
#
# #c.data == "knopka (callback_data="knopka")
# @bot.callback_query_handler(func=lambda c: c.data == "knopka")
# def onKnopka(c):
#     bot.send_message(c.message.chat.id, "Нажата кнопка")
#
# @bot.callback_query_handler(func=lambda c: c.data == "Like")
#  def onKnopka1(c):
#      bot.send_message(c.message.chat.id, "Нажат Like")


