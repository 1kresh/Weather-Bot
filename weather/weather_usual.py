from bot import bot
from report_error import report_error
from helpful_functions.language_defining import language_define
from phrases import (
    take_phrase_1, take_phrase_2)
from weather.weather_main import get_forecast
from weather_menu import weather_menu

from telebot import types

def preparing_1(message):
    try:
        lang_num = language_define(message)
        ask_text = take_phrase_2('place_input', 'today', lang_num)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_geo = types.KeyboardButton(text=take_phrase_1('geolocation', lang_num), request_location=True)        
        keyboard.add(button_geo)
        sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
        bot.register_next_step_handler(sent, weather_1)
    except Exception as e:
        report_error(e)
        weather_menu(message)
def weather_1(message):
    place = message.text
    get_forecast(message, place, 0)
    

def preparing_2(message):
    try:
        lang_num = language_define(message)
        ask_text = take_phrase_2('place_input', 'tomorrow', lang_num)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_geo = types.KeyboardButton(text=take_phrase_1('geolocation', lang_num), request_location=True)
        keyboard.add(button_geo)
        sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
        bot.register_next_step_handler(sent, weather_2)
    except Exception as e:
        report_error(e)
        weather_menu(message)
def weather_2(message):
    place = message.text
    get_forecast(message, place, 1)

def preparing_3(message):
    try:
        lang_num = language_define(message)
        ask_text = take_phrase_2('place_input', 'day_after_tomorrow', lang_num)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_geo = types.KeyboardButton(text=take_phrase_1('geolocation', lang_num), request_location=True)
        keyboard.add(button_geo)
        sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
        bot.register_next_step_handler(sent, weather_3)
    except Exception as e:
        report_error(e)
        weather_menu(message)
def weather_3(message):
    place = message.text
    get_forecast(message, place, 2)

