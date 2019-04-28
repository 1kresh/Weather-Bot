from bot import bot
from helpful_functions.language_defining import language_define
from phrases import (
    take_phrase_1, take_phrase_2)
from report_error import report_error
from weather_menu import weather_menu
from weather.weather_main import get_forecast

from telebot import types


def preparing_0(message, data=None):
    if data: lang_num = 0 if 'Get' in data else 1
    else: lang_num = language_define(message)
        
    ask_text = take_phrase_2('place_input', 'today', lang_num)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text=take_phrase_1('geolocation', lang_num), request_location=True)        
    keyboard.add(button_geo)
    sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
    bot.register_next_step_handler(sent, weather_0)


def weather_0(message, adress=None, lang_num=None):

    place = adress if adress else message.text
    get_forecast(message, place, 0, lang_num)
    

def preparing_1(message):
    lang_num = language_define(message)
    ask_text = take_phrase_2('place_input', 'tomorrow', lang_num)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text=take_phrase_1('geolocation', lang_num), request_location=True)
    keyboard.add(button_geo)
    sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
    bot.register_next_step_handler(sent, weather_1)


def weather_1(message, adress=None):

    place = adress if adress else message.text
    get_forecast(message, place, 1)


def preparing_2(message):
    lang_num = language_define(message)
    ask_text = take_phrase_2('place_input', 'day_after_tomorrow', lang_num)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text=take_phrase_1('geolocation', lang_num), request_location=True)
    keyboard.add(button_geo)
    sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
    bot.register_next_step_handler(sent, weather_2)


def weather_2(message, adress=None):

    place = adress if adress else message.text
    get_forecast(message, place, 2)

