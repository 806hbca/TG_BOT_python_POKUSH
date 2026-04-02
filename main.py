import telebot
import datetime
import pytz
import sqlite3
from telebot import types  # для указание типов
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()

from telebot import apihelper
apihelper.proxy = {'https': os.getenv("PROXY_URL")} if os.getenv("PROXY_URL") else {}

bot = telebot.TeleBot(os.getenv("TOKEN"))

Evening = ''
Morning = ''


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Предложения по улучшению/отзывы")
    btn2 = types.KeyboardButton("Рецепты")
    btn3 = types.KeyboardButton("Водный баланс")
    btn4 = types.KeyboardButton("Полезные статьи")
    markup.add(btn2, btn3, btn4, btn1)
    bot.send_message(message.chat.id,
                     text="Скажи, чем я могу помочь?".format(
                         message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def mistake(message):
    bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован=(..")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Нужно ещё чем-то помочь?".format(
                         message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, start)


def end(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Нужно ещё чем-то помочь?".format(
                         message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, start)


def on_click(message):
    if (message.text == "Предложения по улучшению/отзывы"):
        bot.send_message(message.chat.id, "Введите ваш отзыв")
        bot.register_next_step_handler(message, save_review)
    elif (message.text == "Рецепты"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Я веган")
        btn2 = types.KeyboardButton("Я не веган")
        btn3 = types.KeyboardButton("На диете")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="К какому типу вы относитесь?", reply_markup=markup)
        bot.register_next_step_handler(message, recipe)
    elif (message.text == "Полезные статьи"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Статья про спорт",
                                              url='https://legendame.ru/gorodskoj-lager-xobbixorsing-v-moskve'))
        markup.add(types.InlineKeyboardButton("Статья про питание",
                                              url='https://aif.ru/health/food/kotik_v_meshke_shaurma_potencialno_odin_iz_samyh_poleznyh_fastfudov'))
        markup.add(types.InlineKeyboardButton("Статья про воду", url='https://www.kp.ru/best/ufa/water/'))
        bot.send_message(message.chat.id, text="Полезные статьи", reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да")
        btn2 = types.KeyboardButton("Нет")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         text="Нужно ещё чем-то помочь?".format(
                             message.from_user), reply_markup=markup)
        bot.register_next_step_handler(message, start)

    elif message.text == "Водный баланс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Поставить уведомление")
        btn2 = types.KeyboardButton("Убрать уведомление")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Выберите действие", reply_markup=markup)
        bot.register_next_step_handler(message, woter_b)

    else:
        mistake(message)


def recipe(message):
    if message.text == "Я веган":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Завтрак")
        btn2 = types.KeyboardButton("Обед")
        btn3 = types.KeyboardButton("Ужин")
        btn4 = types.KeyboardButton("Перекус")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text=f"На какой приём пищи?", reply_markup=markup)
        bot.register_next_step_handler(message, recipe1)
    elif message.text == "Я не веган":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Завтрак")
        btn2 = types.KeyboardButton("Обед")
        btn3 = types.KeyboardButton("Ужин")
        btn4 = types.KeyboardButton("Перекус")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text=f"На какой приём пищи?", reply_markup=markup)
        bot.register_next_step_handler(message, recipe2)
    elif message.text == "На диете":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Завтрак")
        btn2 = types.KeyboardButton("Обед")
        btn3 = types.KeyboardButton("Ужин")
        btn4 = types.KeyboardButton("Перекус")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text=f"На какой приём пищи?", reply_markup=markup)
        bot.register_next_step_handler(message, recipe3)
    else:
        mistake(message)


def recipe1(message):
    if message.text == "Завтрак":
        bot.send_message(message.chat.id, text=f"Завтрак_1?")
    elif message.text == "Обед":
        bot.send_message(message.chat.id, text=f"Обед_1?")
    elif message.text == "Ужин":
        bot.send_message(message.chat.id, text=f"Обед_1?")
    elif message.text == "Перекус":
        bot.send_message(message.chat.id, text=f"Перекус 3?")
    else:
        mistake(message)
        return 1
    end(message)


def recipe2(message):
    if message.text == "Завтрак":
        bot.send_message(message.chat.id, text=f"Завтрак 2?")
    elif message.text == "Обед":
        bot.send_message(message.chat.id, text=f"Обед 2?")
    elif message.text == "Ужин":
        bot.send_message(message.chat.id, text=f"Обед 2?")
    elif message.text == "Перекус":
        bot.send_message(message.chat.id, text=f"Перекус 2?")
    else:
        mistake(message)
        return 1
    end(message)


def recipe3(message):
    if message.text == "Завтрак":
        bot.send_message(message.chat.id, text=f"Завтрак 3?")
    elif message.text == "Обед":
        bot.send_message(message.chat.id, text=f"Обед 3?")
    elif message.text == "Ужин":
        bot.send_message(message.chat.id, text=f"Обед 3?")
    elif message.text == "Перекус":
        bot.send_message(message.chat.id, text=f"Перекус 3?")
    else:
        mistake(message)
        return 1
    end(message)


def save_review(message):
    r = message.text
    conn = sqlite3.connect('reviews.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS
                reviews (id int auto_increment primary key, 
                name TEXT NOT NULL, 
                review TEXT NOT NULL)''')
    cur.execute("INSERT INTO reviews(name, review) VALUES('%s','%s')" % (message.chat.id, r))
    conn.commit()
    conn.close()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Нужно ещё чем-то помочь?".format(
                         message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, start)


def woter_b(message):
    if message.text == "Поставить уведомление":
        bot.send_message(message.chat.id,
                         text="Задайте время отпраки уведомления утром в формате чч.мм")
        bot.register_next_step_handler(message, woter_b_1)
    elif message.text == "Убрать уведомление":
        conn = sqlite3.connect('time.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS
                            timetable (id int auto_increment primary key,
                            chat_id INT NOT NULL,
                            Morning TEXT NOT NULL, 
                            Evening TEXT NOT NULL)''')
        cur = conn.cursor()

        cur.execute("SELECT chat_id FROM timetable where chat_id = '%s'" % (str(message.chat.id)))

        if cur.fetchone():
            cur.execute('UPDATE timetable SET Morning=?,Evening=? WHERE chat_id=?', \
                        ("99.99", "99.99", str(message.chat.id)))
            conn.commit()
        else:
            cur.execute("INSERT INTO timetable(chat_id ,Morning, Evening) VALUES('%s','%s','%s')" % \
                        (str(message.chat.id), "99.99", "99.99"))
            conn.commit()
        conn.close()
        bot.send_message(message.chat.id,
                         text="Уведомления успешно убраны")
        end(message)
    else:
        mistake(message)


def woter_b_1(message):
    global Morning
    Morning = str(message.text)
    Morning = Morning.replace(" ", "")
    Morning = Morning.replace(".", ":")
    Morning = Morning.replace(",", ":")
    try:
        p = Morning.split(":")
        datetime.time(int(p[0]), int(p[1]))
    except ValueError:
        bot.send_message(message.chat.id,
                         text="Неверный формат. Попробуйте ещё раз")
        bot.register_next_step_handler(message, woter_b_1)
        return 1
    else:
        bot.send_message(message.chat.id,
                         text="Задайте время отпраки уведомления вечером в формате чч.мм")
        bot.register_next_step_handler(message, woter_b_2)


def woter_b_2(message):
    global Morning
    Evening = str(message.text)
    Evening = Evening.replace(" ", "")
    Evening = Evening.replace(".", ":")
    Evening = Evening.replace(",", ":")
    try:
        p = Evening.split(":")
        datetime.time(int(p[0]), int(p[1]))
    except ValueError:
        bot.send_message(message.chat.id,
                         text="Неверный формат. Попробуйте ещё раз")
        bot.register_next_step_handler(message, woter_b_2)
        return 1

    conn = sqlite3.connect('time.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS
                    timetable (id int auto_increment primary key,
                    chat_id INT NOT NULL,
                    Morning TEXT NOT NULL, 
                    Evening TEXT NOT NULL)''')
    cur = conn.cursor()

    cur.execute("SELECT chat_id FROM timetable where chat_id = '%s'" % (str(message.chat.id)))

    if cur.fetchone():
        cur.execute('UPDATE timetable SET Morning=?,Evening=? WHERE chat_id=?', \
                    (Morning, Evening, \
                     str(message.chat.id)))
        conn.commit()
    else:
        cur.execute("INSERT INTO timetable(chat_id ,Morning, Evening) VALUES('%s','%s','%s')" % \
                    (str(message.chat.id), Morning, Evening))
        conn.commit()
    conn.close()
    end(message)


try:
    bot.set_my_commands([
        types.BotCommand("start", "Запустить бота")
    ])
except Exception:
    pass

bot.polling(none_stop=True)
