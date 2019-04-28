from bot import bot
from dbs.db_filling import (
    check_user, check_user_all, query_add)
from helpful_functions.language_defining import language_define
from helpful_functions.translation import translate
from phrases import (
    take_character_1, take_character_2,
    take_phrase_1, take_phrase_2)
from report_error import report_error
from weather.weather_main import (
    get_coords, get_inf)
from weather_menu import weather_menu

import datetime
from telebot import types


def preparing_week(message):
    n = language_define(message)
    ask_text = take_phrase_2('place_input', 'week', n)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text=take_phrase_1('geolocation', n), request_location=True)
    keyboard.add(button_geo)
    sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
    bot.register_next_step_handler(sent, weather_week)
        
        
def weather_week(message, adress=None):

    place = adress if adress else message.text
    lang_num = language_define(message)

    try: 
        coords = get_coords(message, place)
        town = coords[0]
        if len(coords) == 3: latitude, longitude = coords[1:]
        
        if lang_num == 0: town = translate(town, lang_num)
        
        weather_inf = get_inf(lang_num, latitude, longitude)
         
        full_inf = ''
        date = datetime.date.today() - datetime.timedelta(days=1)
        
        type_str = take_character_1('type', lang_num)
        temperature_max_str = take_character_2('temperature', 'max', lang_num)
        temperature_min_str = take_character_2('temperature', 'min', lang_num)
        
        for n in range(8):
            date += datetime.timedelta(days=1)
            try:
                subjects = weather_inf['daily']['data'][n]

                summary = subjects['summary']

                keys_ = subjects.keys()
                precipType = subjects['precipType'] if 'precipType' in keys_ else ''
                if (lang_num == 1 and precipType): precipType = translate(precipType)
                temperatureHigh = round(5/9 * (subjects['temperatureHigh']-32)) if 'temperatureHigh' in keys_ else ''
                temperatureLow = round(5/9 * (subjects['temperatureLow']-32)) if 'temperatureLow' in keys_ else ''
                inf = f'{date}, {town}:\n{summary}{type_str}{precipType}\
                        {"%s%s°C" % (temperature_max_str, temperatureHigh) if temperatureHigh else ""}\
                        {"%s%s°C" % (temperature_min_str, temperatureLow) if temperatureLow else ""}'
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(*[types.InlineKeyboardButton(text=word, callback_data=f'{word}&{lang_num}&{town}&{date}') for word in [take_phrase_1('more', lang_num)]])
                bot.send_message(message.chat.id, inf, reply_markup=keyboard)
            except KeyError:
                inf = f'{date} {town}:\n{language_1("errors", "top_0_error", lang_num)}'
                bot.send_message(message.chat.id, inf)
            full_inf += inf
            
    except Exception as e:
        town = place
        full_inf = ''
        bot.send_message(message.chat.id, take_phrase_2('errors', 'top_error', lang_num))
    
    try:      
        check_user(message)
        check_user_all(message)
        query_add(message, 'Неделя', town, full_inf, '', '')    
    except Exception as e:
        report_error(e) 
    weather_menu(message)

