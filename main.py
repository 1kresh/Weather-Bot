#Hello!
#This is a  bot which was created to inform you about the weather.
#Здравствуйте!
#Это бот, который создан для оповещения вас о погоде.

from bot import bot
from dbs.db_creating import prepare_db
from dbs.db_filling import (
    check_user, check_user_all, check_user_new
    check_user_all_new, query_add)
from dbs.db_filling_main import make_query
from df_token import df_token
from game_towns.game import preparing_game
from game_towns.parsing import towns_parsing
from helpful_functions.language_defining import language_define
from menu import menu
from phrases import (
    phrases, take_phrase_1, take_phrase_2)
from reading_of_messages import choosing
from report_error import report_error
from statistic.queries import (
    get_query_today, get_query_all)
from statistic.users import (
    get_users_today, get_users_all)
from stat_menu import stat_menu
from weather_menu import weather_menu
from weather.weather_main import (
    get_inf, get_main_parts, 
    get_coords, name_define)
from weather.weather_now import preparing
from weather.weather_usual import (
    preparing_0, preparing_1, preparing_2)
from weather.weather_week import preparing_week

import apiai
from bs4 import BeautifulSoup
import collections
import datetime
import json
import os
import random
import requests
import sqlite3
import telebot
from telebot import types
import time
from time import sleep
import urllib
import urllib.request


@bot.message_handler(commands=['start'])
def start(message):
    try:
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
    ID = message.from_user.id
    lang_num = language_define(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(take_phrase_1('menu', lang_num))
    markup.row(take_phrase_1('settings', lang_num))
    start_text = take_phrase_1('start', lang_num)
    
    bot.send_message(message.chat.id, start_text, reply_markup=markup)
        

def languages_f(message, word=None):
    if word: lang_num = 1 if 'рус' in word.lower() else 0
    else: lang_num = 1 if 'рус' in message.text.lower() else 0

    check_user_all_new(message, take_phrase_1('languages_type', lang_num))
    make_query('update Users_new set lang = "{}"'.format(take_phrase_1('languages_type', lang_num)))   
    bot.send_message(message.chat.id, text=take_phrase_1('langs', lang_num)+take_phrase_1('languages_type', lang_num))
    if message.text == 'Русский(ru)' or message.text == 'English(en)':
        start_menu(message)
    else:
        settings(message)
    
        
def settings(message):
    lang_num = language_define(message)
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.row(take_phrase_1('languages_o', lang_num))
    markup.row(take_phrase_1('developing', lang_num))
    markup.row(take_phrase_1('back', lang_num))
    bot.send_message(message.chat.id, take_phrase_1('choose', lang_num), reply_markup=markup)
    

def languages_set(message):
    lang_num = language_define(message)
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.row('Русский', 'English')
    markup.row(take_phrase_1('back_settings', lang_num), take_phrase_1('back_start', lang_num))
    bot.send_message(message.chat.id, take_phrase_1('language', lang_num), reply_markup=markup)   
    

def developing(message):
    bot.send_message(message.chat.id, '@kresh_one')    


def text_message_processing(text, lang):
    request = apiai.ApiAI(df_token).text_request() 
    request.lang = lang
    request.session_id = 'WeatherBotHelper_ai'
    request.query = text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    
    try: response = responseJson['result']['parameters']
    except: return [], None
        
    response_values = list(filter(lambda x: response[x] != '', list(response)))
    _list, address = [responseJson['result']['contexts'][0]['name']], None

    for value in response_values:
        if value == 'date-time':
            now = datetime.datetime.now()
            try:
                then = datetime.datetime(*map(int, response[value].split('-')))
            except:
                then = datetime.datetime(*map(int, (response[value].split('/')[1]).split('-')))
            delta = then - now
            days = delta.days
            if days == -1: _list.append('today')
            elif days == 0: _list.append('tommorow')
            elif days == 1: _list.append('after tommorow')
            elif days == 6: _list.append('week')
            else: _list.append('now')
        elif value == 'langs': _list.append(response[value])
        elif value == 'address': address = list(response[value].values())[0]
        else: _list.append(value)
    
    return list(set(_list)), address 


@bot.message_handler(content_types=["text"])
def text_receiving(message):
    t = message.text 
    ID = message.from_user.id
    lang_num = language_define(message)
    if t == 'Сейчас' or t == 'Now':
        preparing(message)
    elif t == 'Сегодня' or t == 'Today':
        preparing_0(message)
    elif t == 'Завтра' or t == 'Tomorrow':
        preparing_1(message)
    elif t == 'Послезавтра' or t == 'Day after tomorrow':
        preparing_2(message)
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
    else:
        _list, address = text_message_processing(t, 'ru' if lang_num else 'en')
        if 'rus' in _list:
            languages_f(message, 'рус')
        elif 'en' in _list:
            languages_f(message, 'англ')
        elif 'developer' in _list:
            developing(message)
        elif 'game' in _list and language_define(message) == 1:
            game(message)
        elif 'top' in _list and language_define(message) == 1:
            top(message)
        elif 'lang' in _list:
            languages_set(message)
        elif 'settings' in _list:
            settings(message)
        elif _list:
            choosing(message, _list, address)
        else:
            bot.send_message(message.chat.id, take_phrase_1('n_u', lang_num)) 
            start_menu(message)
        

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'Подробнее':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=phrases['game']['advanced_rules'], parse_mode='Markdown')
    elif c.data == 'Информация':
        c_req = (c.message.text).strip().split()
        town = c_req[-1]

        if len(c_req) == 5: town = f'{c_req[3]}_{c_req[4]}'
        elif len(c_req) == 2: town =  f'{c_req[0]}_{c_req[1]}'

        db_inf = make_query('select inf from Inf_towns where town=?', (town, ))
        
        if len(db_inf) != 0:
            text = db_inf[0][0]
        else:
            req = requests.get(f'https://ru.wikipedia.org/wiki/{town}').text
            soup = BeautifulSoup(req, 'html.parser')
            all_p = soup.find_all('p')
            try:
                inf_extra = (all_p[0]).text
                if 'отпатрулирована' in inf_extra: inf_extra = (all_p[1]).text
                inf_extra = inf_extra.strip().split()
                inf = ''
                
                for j in range(2):
                    for part in inf_extra:
                        l, r = part.find('['), part.find(']')
                        if l != -1: part = part.replace(part[l:r+1], '')
                        inf += f'{part} '

                if 'фамилия' in inf or 'населённых пунктов' in inf: raise Exception
                else: text = phrases['game']['all_inf'].format(inf, town)

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
            inf = ''
        try:
            check_user(c.message)
            check_user_all(c.message)
            query_add(c.message, name, town, inf, '', '')
        except Exception as e:
            report_error(e) 

    elif 'Get weather' in c.data or 'Получить погоду' in c.data:
        address = c.data.strip().split('|')[-1]
        if address != 'None': weather_0(c.message, address, lang_num=0 if 'Get' in c.data else 1)
        else: preparing_0(c.message, c.data)

    elif 'Get statistics'  in c.data or 'Получить статистику' in c.data:
        lang_num = 0 if 'Get' in c.data else 1
        text = take_phrase_1('stats_text_pq_2', lang_num)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(take_phrase_2('statistic', 'today_users', lang_num), take_phrase_2('statistic', 'today_requests', lang_num))
        markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
        bot.send_message(c.message.chat.id, text, reply_markup=markup)         
    else:
        bot.send_message(c.message.chat.id, 'C Error')
    

def game(message):
    answer = phrases['game']['short_rules']
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Подробнее']])
    bot.send_message(message.chat.id, answer, reply_markup=keyboard, parse_mode='Markdown')
    
    preparing_game(message)
    

def top(message):
    people = [human[0] for human in make_query('select Name from Winners')]
    results = collections.Counter(people).most_common()
    
    text = 'Пользователь | Кол-во побед\n'
    for result in results:
        text += f'{result[0]} | {result[1]}\n'

    bot.send_message(message.chat.id, text)


def main():
    try: bot.polling(none_stop=True, interval=0)
    except Exception as e: report_error(e)


if __name__ == '__main__': 
    prepare_db()
    towns_parsing()
    while True:
        try: main()
        except: sleep(1)


