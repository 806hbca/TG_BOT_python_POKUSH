import telebot
import datetime
import sqlite3
import schedule
import time
import os
import pytz
from dotenv import load_dotenv, dotenv_values
load_dotenv()

from telebot import apihelper
apihelper.proxy = {'https': os.getenv("PROXY_URL")} if os.getenv("PROXY_URL") else {}

bot=telebot.TeleBot(os.getenv("TOKEN"))

MOSCOW_TZ = pytz.timezone('Europe/Moscow')

bd={}

def create_time_bd():
    conn = sqlite3.connect('time.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS
                        timetable (id int auto_increment primary key,
                        chat_id INT NOT NULL,
                        Morning TEXT NOT NULL, 
                        Evening TEXT NOT NULL)''')
    conn.commit()
    conn.close()
def obnovlenee_bd():
    conn = sqlite3.connect('time.db')
    cur = conn.cursor()
    sqlite_select_query = """SELECT * from timetable"""
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for x in records:
        if x[2] in bd:
            bd[x[2]].add(x[1])
        else:
            bd[x[2]]=set()
            bd[x[2]].add(x[1])
        if x[3] in bd:
            bd[x[3]].add(x[1])
        else:
            bd[x[3]]=set()
            bd[x[3]].add(x[1])

def send_m(a):
    bot.send_message(a,"Попей воды")

def pre_send():
    d=datetime.datetime.now(MOSCOW_TZ)
    p=d.strftime('%H:%M')

    if p in bd:
        for x in bd[p]:
            send_m(x)

create_time_bd()
obnovlenee_bd()
schedule.every(1).minutes.do(pre_send)
schedule.every(1).minutes.do(obnovlenee_bd)

while True:
    schedule.run_pending()
    time.sleep(1)
