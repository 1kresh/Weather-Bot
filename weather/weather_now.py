from bot import bot
from report_error import report_error
from dbs.db_filling import (
    query_add, check_user, check_user_all)
from helpful_functions.language_defining import language_define
from phrases import (
    take_phrase_1, take_phrase_2, take_character_2)
from weather.weather_main import ( 
    get_coords, get_inf, words)
from searching.pictures_searching import get_photo
from searching.poems_searching import get_poem
from weather_menu import weather_menu
from helpful_functions.translation import translate

from telebot import types
import datetime

def preparing(message):
    try:
        print(2)
        lang_num = language_define(message)
        ask_text = take_phrase_2('place_input', 'now', lang_num)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_geo = types.KeyboardButton(text=take_phrase_1('geolocation', lang_num), request_location=True)
        keyboard.add(button_geo)
        sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
        bot.register_next_step_handler(sent, weather)
    except Exception as e:
        report_error(e)
        weather_menu(message)
        
        
def weather(message):
    print(6)
    place = message.text
    lang_num = language_define(message)

    coords = get_coords(message, place)
    town = coords[0]
    if len(coords) == 3: latitude, longitude = coords[1:]

    try:
        weather_inf = get_inf(lang_num, latitude, longitude)   
        
        subjects = weather_inf['currently']

        summary = subjects['summary']
        humidity = round(subjects['humidity']*100)
        windSpeed = round(subjects['windSpeed']*0.447)
        windGust = round(subjects['windGust']*0.447)
        pressure = round(subjects['pressure']*0.75006)
        time = datetime.datetime.now(tz=None)
        time = str((time+datetime.timedelta(hours=3)) if lang_num == 1 else time).split('.')[0]
        current_time = take_phrase_2('weather', 'now', lang_num)
        time_name = take_character_2('time_all', 'time', lang_num)
        temperature_name = take_character_2('temperature', 'usual', lang_num)
        temperature_feeling_name = take_character_2('temperature', 'feeling', lang_num)

        timezone, precipType_name, humidity_name, wind_name, wind_max_name, wind_unit, pressure_name, pressure_unit, visibility_name, visibility_unit = words(lang_num)
    
        if lang_num == 0: town = translate(town, lang_num)

        keys_ = subjects.keys()

        precipType = subjects['precipType'] if 'precipType' in keys_ else ''
        if lang_num == 1 and precipType: precipType = translate(precipType)

        temperature = round(5/9 * (subjects['temperature']-32)) if 'temperature' in keys_ else ''
        apparentTemperature = round(5/9 * (subjects['apparentTemperature']-32)) if 'apparentTemperature' in keys_ else ''

        visibility = round(subjects['visibility']*1.61, 1) if 'visibility' in keys_ else ''
        
        search_term = f'{town} {precipType}'

        inf = f'{current_time}, {town}:{time_name}{time}{timezone}\n{summary}{precipType_name}{precipType}\
                {humidity_name}{humidity}%{"%s%s°C" % (temperature_name, temperature) if temperature else ""}\
                {"%s%s°C" % (temperature_feeling_name, apparentTemperature) if apparentTemperature else ""}\
                {wind_name}{windSpeed}{wind_unit}{wind_max_name}{windGust}{wind_unit}\
                {pressure_name}{pressure}{pressure_unit}{visibility_name}{visibility}{visibility_unit}'
        
        bot.send_message(message.chat.id, inf)
    except Exception as e:
        search_term = town
        inf = '' 
        bot.send_message(message.chat.id, take_phrase_2('errors', 'top_error', lang_num))
        report_error(e.args)
           
    thumbnail_url = get_photo(message, search_term)
    #poem = get_poem(message, precipType, summary, search_term)

    try:
        check_user(message)
        check_user_all(message)
        query_add(message, 'Сейчас', town, inf, thumbnail_url, poem) 
    except Exception as e:
        report_error(e) 
        
    weather_menu(message)

