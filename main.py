#Hello!
#This is a  bot which was created to inform you about the weather.
#Здравствуйте!
#Это бот, который создан для оповещения вас о погоде.
from bot import bot
from report_error import report_error
from phrases import (
    phrases, take_phrase_1, take_phrase_2)
from dbs.db_creating import prepare_db
from dbs.db_filling import (
    query_add, check_user, 
    check_user_all, check_user_new, 
    check_user_all_new)
from dbs.db_filling_main import make_query
from weather.weather_main import (
    get_inf, get_main_parts, 
    get_coords, name_define)
from weather.weather_now import preparing
from weather.weather_week import preparing_week
from weather.weather_usual import (
    preparing_1, preparing_2, preparing_3)
from statistic.queries import (
    get_query_today, get_query_all)
from statistic.users import (
    get_users_today, get_users_all)
from game_towns.game import preparing_game
from game_towns.parsing import towns_parsing
from reading_of_messages import l_w
from training_of_basic_model import (
    adding, deleting_0,
    deleting_01, output_0,
    checking)
from helpful_functions.language_defining import language_define
from weather_menu import weather_menu
from menu import menu

import telebot
import json
import os
from telebot import types
import datetime 
import random
import sqlite3
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import time
from time import sleep
import collections


@bot.message_handler(commands=['dev'])
def devel(message):
    try:
        if message.from_user.id == 450398500:
            evolving(message)
        else:
            pass
    except Exception as e:
        report_error(e)
        weather_menu(message)    

def weather_or_stat_today(message, last_words):
    try:
        lang_num = language_define(message)
        ask_text = take_phrase_1('weather_or_stat', lang_num)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=f"{name} {('_'.join(last_words) if last_words != None else 'None')}") for name in [take_phrase_2('quests', 'weather', lang_num), take_phrase_2('quests', 'stats', lang_num)]])
        bot.send_message(message.chat.id, ask_text, reply_markup = keyboard)
    except Exception as e:
        report_error(e)
        weather_menu(message)
        
def stats_people(message):
    try:
        lang_num = language_define(message)
        text = take_phrase_1('stats_text_p', lang_num)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(take_phrase_2('statistic', 'today_users', lang_num), take_phrase_2('statistic', 'all_users', lang_num))
        markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
        bot.send_message(message.chat.id, text, reply_markup=markup) 
    except Exception as e:
        report_error(e)
        
def stats_queries(message):
    try:
        lang_num = language_define(message)
        text = take_phrase_1('stats_text_q', lang_num)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(take_phrase_2('statistic', 'today_requests', lang_num), take_phrase_2('statistic', 'all_requests', lang_num))
        markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
        bot.send_message(message.chat.id, text, reply_markup=markup) 
    except Exception as e:
        report_error(e)
        
def stats_today(message):
    try:
        lang_num = language_define(message)
        text = take_phrase_1('stats_text_pq_all', lang_num)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(take_phrase_2('statistic', 'all_users', lang_num), take_phrase_2('statistic', 'all_requests', lang_num))
        markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
        bot.send_message(message.chat.id, text, reply_markup=markup) 
    except Exception as e:
        report_error(e)
        
def stats_all(message):
    try:
        lang_num = language_define(message)
        text = take_phrase_1('stats_text_pq_today', lang_num)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(take_phrase_2('statistic', 'today_users', lang_num), take_phrase_2('statistic', 'today_requests', lang_num))
        markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
        bot.send_message(message.chat.id, text, reply_markup=markup) 
    except Exception as e:
        report_error(e)
        
        
def evolving(message):
    try:
        lang_num = language_define(message)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.row(take_phrase_1('adding', lang_num), take_phrase_1('checking', lang_num))
        markup.row(take_phrase_1('deleting_t', lang_num), take_phrase_1('deleting_w', lang_num))
        markup.row(take_phrase_1('outputing', lang_num))
        markup.row(take_phrase_1('back_start', lang_num))
        bot.send_message(message.chat.id, take_phrase_1('choosing', lang_num), reply_markup=markup)
    except Exception as e:
        report_error(e)
        weather_menu(message) 
        
@bot.message_handler(commands=['start'])
def start(message):
    print(12)
    try:
        #make_query('Drop table if exists Users_All_new')
        #make_query('Drop table if exists Users_new')
        
        #print(make_query('select * from Users_new'))
        check_user_all_new(message, 'English')
        check_user_new(message, 'English')
        
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.row(take_phrase_1('languages_type_1', 1), take_phrase_1('languages_type_1', 0))
        start_text = phrases["start_text"]
        
        bot.send_message(message.chat.id, start_text, reply_markup=markup)  
           
    except Exception as e:
        report_error(e)
        
@bot.message_handler(commands=['help'])
def start_menu(message):
    print(11)
    try:
        ID = message.from_user.id
        lang_num = language_define(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(take_phrase_1('menu', lang_num))
        markup.row(take_phrase_1('settings', lang_num))
        if ID == 450398500:
            markup.row(take_phrase_1('developing1', lang_num))
        start_text = take_phrase_1('start', lang_num)
        
        bot.send_message(message.chat.id, start_text, reply_markup=markup)    
        
    except Exception as e:
        report_error(e)
        
def languages_f(message, word=None):
    print(10)
    lang_num = 1 if 'рус' in message.text.lower() else 0
    check_user_all_new(message, take_phrase_1('languages_type', lang_num))
    make_query('update Users_new set lang = "{}"'.format(take_phrase_1('languages_type', lang_num)))   
    bot.send_message(message.chat.id, text=take_phrase_1('langs', lang_num)+take_phrase_1('languages_type', lang_num))
    if message.text == 'Русский(ru)' or message.text == 'English(en)':
        start_menu(message)
    else:
        settings(message)
    
        
def settings(message):
    print(8)
    lang_num = language_define(message)
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.row(take_phrase_1('languages_o', lang_num))
    markup.row(take_phrase_1('developing', lang_num))
    markup.row(take_phrase_1('back', lang_num))
    bot.send_message(message.chat.id, take_phrase_1('choose', lang_num), reply_markup=markup)
    
def languages_set(message):
    print(7)
    lang_num = language_define(message)
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.row('Русский', 'English')
    markup.row(take_phrase_1('back_settings', lang_num), take_phrase_1('back_start', lang_num))
    bot.send_message(message.chat.id, take_phrase_1('language', lang_num), reply_markup=markup)   
    
def developing(message):
    print(6)
    bot.send_message(message.chat.id, '@AndreyKorokhov')    
        
def stat_menu(message):
    print(5)
    try:
        lang_num = language_define(message)
        text = take_phrase_2('statistic', 'stats_text', lang_num)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(take_phrase_2('statistic', 'today_users', lang_num), take_phrase_2('statistic', 'all_users', lang_num))
        markup.row(take_phrase_2('statistic', 'today_requests', lang_num), take_phrase_2('statistic', 'all_requests', lang_num))
        if lang_num == 1:
            markup.row('Рейтинг игроков🏆')
        markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
        bot.send_message(message.chat.id, text, reply_markup=markup) 
    except Exception as e:
        report_error(e)
        
@bot.message_handler(content_types=["text"])
def text_receiving(message):
    print(4)
    t = message.text 
    ID = message.from_user.id
    #print(make_query('select * from Users_new'))
    #print(make_query('select * from Users'))
    if t == 'Сейчас' or t == 'Now':
        print(3)
        preparing(message)
    elif t == 'Сегодня' or t == 'Today':
        print(6)
        preparing_1(message)
    elif t == 'Завтра' or t == 'Tomorrow':
        preparing_2(message)
    elif t == 'Послезавтра' or t == 'Day after tomorrow':
        preparing_3(message)
    elif t == 'Неделя' or t == 'Week':
        preparing_week(message)
    elif t == 'Кол-во пользователей за сегодня' or t == 'Number of users today':
        get_users_today(message)
    elif t == 'Кол-во пользователей за все время' or t == 'Number of all users':
        get_users_all(message)
    elif t == 'Кол-во запросов за сегодня' or t == 'Number of requests today':
        get_query_today(message)
    elif t == 'Кол-во запросов за все время' or t == 'Number of all requests':
        get_query_all(message)
    elif t == '⬅️Назад(Меню)' or t == 'Меню📋' or t == 'Menu📋' or t == '⬅️Back(Menu)':
        menu(message)
    elif t == 'Получить погоду🌤' or t == 'Get weather🌤':
        weather_menu(message)
    elif t == 'Получить статистику📈' or t == 'Get statistics📈':
        stat_menu(message)
    elif t == 'Игра в города👾':
        game(message)
    elif t == 'Рейтинг игроков🏆':
        top(message)
    elif t == 'English' or t == 'Русский' or t == 'English(en)' or t == 'Русский(ru)':
        languages_f(message)
    elif t == 'Настройки⚙️' or t == 'Settings⚙️' or t == '⬅️Back(Settings)' or t == '⬅️Назад(Настройки)':
        settings(message)
    elif t == 'Language🌏' or t == 'Язык🌏':
        languages_set(message)
    elif t == '⬅️Back' or t == '⬅️Назад' or t == '⬅️Назад(Начало)' or t == '⬅️Back(Start)':
        start_menu(message)
    elif t == 'Creator👨🏻‍💻' or t == 'Разработчик👨🏻‍💻':
        developing(message)
    elif ID == 450398500:
        if t == 'Creator' or t == 'Разработчик':
            evolving(message)
        elif t == 'Add' or t == 'Добавить':
            adding(message)
        elif t == 'Check' or t == 'Проверить':
            checking(message)
        elif t == 'Delete type' or t == 'Удалить тип':
            deleting_0(message)
        elif t == 'Delete word' or t == 'Удалить слово':
            deleting_01(message)
        elif t == 'Output' or t == 'Вывод':
            output_0(message)
        elif t == 'Back👨🏻‍💻' or t == 'Назад👨🏻‍💻':
            evolving(message)   
    else:
        start_menu(message)
        
@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    print(3)
    if c.data == 'Подробнее':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=phrases['game']['advanced_rules'], parse_mode='Markdown')
    elif c.data == 'Информация':
        c_req = (c.message.text).strip().split()
        town = c_req[-1]
        if len(c_req) == 5:
            town = f'{c_req[3]}_{c_req[4]}'
        elif len(c_req) == 2:
            town =  f'{c_req[0]}_{c_req[1]}'
        
        db_inf = make_query(f'select inf from Inf_towns where town="{town}"')
        if len(db_inf) != 0:
            text = db_inf[0][0]
        else:
            req = requests.get(f'https://ru.wikipedia.org/wiki/{town}').text
            soup = BeautifulSoup(req, 'html.parser')
            all_p = soup.find_all('p')

            try:
                #if '́' in ((all_p[0]).text).strip().split()[0]:
                inf_extra = (all_p[0]).text
                #else:
                #    inf_extra = (all_p[1]).text

                inf_extra = inf_extra.strip().split()
                inf = ''
                for j in range(2):
                    for part in inf_extra:
                        l, r = part.find('['), part.find(']')
                        if l != -1: part = part.replace(part[l:r+1], '')
                        inf += f'{part} '

                if 'фамилия' in inf or 'населённых пунктов' in inf:
                    raise Exception
                else:
                    text = phrases['game']['all_inf'].format(inf, town)

                make_query(f'insert into Inf_towns (town, inf) values ("{town}", "{text}")')
            
            except Exception:
                text = phrases['game']['no_inf'].format(' '.join(town.split('_')), town)
                
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=text, parse_mode='Markdown')
        
    elif 'Больше' in c.data or 'More' in c.data:
        _, lang_num, town, date = (c.data).split('&')
        lang_num, date = int(lang_num), list(map(int, date.split('-')))
        date = datetime.date(day=date[2], month=date[1], year=date[0])
        n = (date - datetime.date.today()).days
        
        try:
            coords = get_coords(c.message, town)
            town = coords[0]
            if len(coords) == 3: latitude, longitude = coords[1:]
            name = name_define(n, lang_num)
            weather_inf = get_inf(lang_num, latitude, longitude)   
            precipType_ru, summary, search_term, inf = get_main_parts(n, lang_num, town, weather_inf, name)

            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=inf, parse_mode='Markdown')
            
        except Exception as e:
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=take_phrase_2('errors', 'top_error', lang_num))
            report_error(e)
            inf = ''

        try:      
            check_user(c.message)
            check_user_all(c.message)
            query_add(c.message, name, town, inf, '', '')    
        except Exception as e:
            report_error(e) 

    elif 'Get weather' in c.data or 'Получить погоду' in c.data:
        last_words = c.data.strip().split()[-1]
        l_w(c.message, 'сегодня', last_words.split('_') if last_words != 'None' else None)
    elif 'Get statistics'  in c.data or 'Получить статистику' in c.data:
        l_pq_1(c.message)           
    else:
        bot.send_message(c.message.chat.id, 'C Error')
    
def game(message):
    print(2)
    answer = phrases['game']['short_rules']
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Подробнее']])
    bot.send_message(message.chat.id, answer, reply_markup=keyboard, parse_mode='Markdown')
    
    preparing_game(message)
    
def top(message):
    print(1)
    people = [human[0] for human in make_query('select Name from Winners')]
    results = collections.Counter(people).most_common()
    
    text = 'Пользователь | Кол-во побед\n'
    for result in results:
        text += f'{result[0]} | {result[1]}\n'

    bot.send_message(message.chat.id, text)
            
def main():
    print(2)
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)
     
if __name__ == '__main__': 
    prepare_db()
    towns_parsing()
    while True:
        try:
            main()
        except:
            sleep(1)


