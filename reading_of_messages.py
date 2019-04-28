from bot import bot
from helpful_functions.language_defining import language_define
from menu import menu
from phrases import (
    phrases, take_phrase_1, take_phrase_2)
from stat_menu import stat_menu
from statistic.queries import (
    get_query_all, get_query_today)
from statistic.users import (
    get_users_all, get_users_today)
from weather_menu import weather_menu
from weather.weather_now import preparing
from weather.weather_usual import (
    preparing_0, preparing_1, preparing_2,
    weather_0, weather_1, weather_2)
from weather.weather_week import preparing_week

from telebot import types


def choosing(message, _list, address=None):
    if 'menu' in _list and len(_list) == 1:
        menu(message)
    else:
        if 'tommorow' in _list:
            weather4(message, 'tommorow', address)   
        elif 'after tommorow' in _list:
            weather4(message, 'after tommorow', address)
        elif 'week' in _list:
            weather4(message, 'week', address)
        elif 'now' in _list:
            weather4(message, 'now', address)
        elif 'all time' in _list:
            if 'queries' in _list:
                get_query_all(message)
            elif 'users' in _list:
                get_users_all(message)
            else:
                users_queries_all(message)
        elif 'today' in _list:
            if 'weather' in _list:
                weather4(message, 'today', address)
            elif 'queries' in _list:
                get_query_today(message)
            elif 'users' in _list:
                get_users_today(message) 
            elif 'statistics'  in _list:
                users_queries_today(message)
            else:
                weather_or_stat(message, address)
        elif 'users' in _list:
            users4(message)
        elif 'queries' in _list:
            queries4(message)
        elif 'statistics' in _list:
            stat_menu(message)
        elif 'weather' in _list:
            weather_menu(message)
        else:
            not_understand(message)
            menu(message)
        

def weather4(message, time, address=None):
    n = dop_name_reverse(time)
    eval(f'weather{n}(message, address)' if address else f'preparing{n}(message)')


def users4(message):
    lang_num = language_define(message)
    text = take_phrase_2('statistic', 'stats_text_p', lang_num)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(take_phrase_2('statistic', 'today_users', lang_num), take_phrase_2('statistic', 'all_users', lang_num))
    markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
    bot.send_message(message.chat.id, text, reply_markup=markup)


def queries4(message):
    lang_num = language_define(message)
    text = take_phrase_2('statistic', 'stats_text_q', lang_num)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(take_phrase_2('statistic', 'today_requests', lang_num), take_phrase_2('statistic', 'all_requests', lang_num))
    markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
    bot.send_message(message.chat.id, text, reply_markup=markup)


def users_queries_all(message):
    lang_num = language_define(message)
    text = take_phrase_1('statistic', 'stats_text_pq_all', lang_num)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(take_phrase_2('statistic', 'all_users', lang_num), take_phrase_2('statistic', 'all_requests', lang_num))
    markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
    bot.send_message(message.chat.id, text, reply_markup=markup)


def users_queries_today(message):
    lang_num = language_define(message)
    text = take_phrase_2('statistic', 'stats_text_pq_today', lang_num)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(take_phrase_2('statistic', 'today_users', lang_num), take_phrase_2('statistic', 'today_requests', lang_num))
    markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
    bot.send_message(message.chat.id, text, reply_markup=markup)


def weather_or_stat(message, address):
    lang_num = language_define(message)
    ask_text = take_phrase_1('weather_or_stat', lang_num)

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(
                types.InlineKeyboardButton(text=take_phrase_2('quests', 'weather', lang_num), callback_data=take_phrase_2('quests', 'weather', lang_num)+'|'+(address if address else 'None')),  
                types.InlineKeyboardButton(text=take_phrase_2('quests', 'stats', lang_num), callback_data=take_phrase_2('quests', 'stats', lang_num))
                    )
                
    bot.send_message(message.chat.id, ask_text, reply_markup = keyboard)


def not_understand(message):
    lang_num = language_define(message)
    bot.send_message(message.chat.id, take_phrase_1('n_u', lang_num))


def dop_name_reverse(time):
    if time == 'now':
        return ''
    elif time == 'today':
        return '_0'
    elif time == 'tommorow':
        return '_1'
    elif time == 'after tommorow':
        return '_2'
    elif time == 'week':
        return '_week'
    else:
        return ''


        

