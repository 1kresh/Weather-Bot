from bot import bot
from report_error import report_error
from helpful_functions.language_defining import language_define
from phrases import (
    take_phrase_2, take_character_1, take_character_2)
from weather.weather_key import weather_key
from helpful_functions.translation import translate
from searching.pictures_searching import get_photo
from searching.poems_searching import get_poem
from dbs.db_filling import (
    query_add, check_user, check_user_all)
from weather_menu import weather_menu

import json
import requests
import datetime
import time

def get_inf(lang_num, latitude, longitude):
    lang = f"lang={'en' if lang_num == 0 else 'ru'}"
    
    weather_inf = requests.get(f'https://api.darksky.net/forecast/{weather_key}/{latitude},{longitude}?{lang}').json()

    return weather_inf

def get_main_parts(n, lang_num, town, weather_inf, name):
    subjects = weather_inf['daily']['data'][n]

    summary = subjects['summary']
    humidity = round(subjects['humidity']*100)
    windSpeed = round(subjects['windSpeed']*0.447)
    windGust = round(subjects['windGust']*0.447)
    pressure = round(subjects['pressure']*0.75006)

    sunriseTime = time.localtime(subjects['sunriseTime'])
    sunriseTime = datetime.datetime(*sunriseTime[:5])
    sunriseTime = str(sunriseTime+datetime.timedelta(hours=3) if lang_num == 1 else sunriseTime)[:-3]

    sunsetTime = time.localtime(subjects['sunsetTime'])
    sunsetTime = datetime.datetime(*sunsetTime[:5])
    sunsetTime = str(sunsetTime+datetime.timedelta(hours=3) if lang_num == 1 else sunsetTime)[:-3]

    sunrise = take_character_2('time_all', 'sunrise', lang_num)
    sunset = take_character_2('time_all', 'sunset', lang_num)
    temperature_max_name = take_character_2('temperature', 'max', lang_num)
    temperature_min_name = take_character_2('temperature', 'min', lang_num)

    timezone, precipType_name, humidity_name, wind_name, wind_max_name, wind_unit, pressure_name, pressure_unit, visibility_name, visibility_unit = words(lang_num)
    
    keys_ = subjects.keys()

    precipType = subjects['precipType'] if 'precipType' in keys_ else ''
    if lang_num == 1 and precipType: precipType = translate(precipType)

    temperatureHigh = round(5/9 * (subjects['temperatureHigh']-32)) if 'temperatureHigh' in keys_ else ''
    temperatureLow = round(5/9 * (subjects['temperatureLow']-32)) if 'temperatureLow' in keys_ else ''

    visibility = round(subjects['visibility']*1.61, 1) if 'visibility' in keys_ else ''
    
    search_term = f'{town}  {precipType}'

    inf = f'{name}, {town}:\n{summary}{sunrise}{sunriseTime}{timezone}\
            {sunset}{sunsetTime}{timezone}{precipType_name}{precipType}{humidity_name}{humidity}%\
            {"%s%s°C" % (temperature_max_name, temperatureHigh) if temperatureHigh else ""}\
            {"%s%s°C" % (temperature_min_name, temperatureLow) if temperatureLow else ""}\
            {wind_name}{windSpeed}{wind_unit}{wind_max_name}{windGust}{wind_unit}\
            {pressure_name}{pressure}{pressure_unit}{visibility_name}{visibility}{visibility_unit}'
    
    return precipType, summary, search_term, inf

def get_coords(message, place):
    try:
        longitude, latitude = message.location.longitude, message.location.latitude
        geocode_inf = requests.get(f'https://geocode-maps.yandex.ru/1.x/?geocode={longitude},{latitude}&format=json').json()
        town = geocode_inf['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][4]['name']
        return town, latitude, longitude
    except AttributeError:
        geocode_req = requests.get(f'https://geocode-maps.yandex.ru/1.x/?geocode={place}&format=json').json()
        geocode_inf = geocode_req['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        longitude, latitude = (geocode_inf['Point']['pos']).split()
        town = geocode_inf['name']
        return town, latitude, longitude
    except:
        return place # town        
    
def name_define(n, lang_num):
    if n == 0:
        name = take_phrase_2('weather', 'today', lang_num)
    elif n == 1:
        name = take_phrase_2('weather', 'tomorrow', lang_num)
    elif n == 2:
        name = take_phrase_2('weather', 'day_after_tomorrow', lang_num)
    elif n == 3 or n == 4:
        name = f"{take_phrase_2('weather', 'after', lang_num)}{n} {take_phrase_2('weather', 'days_1', lang_num)}"
    elif n == 5 or n == 6:
        name = f"{take_phrase_2('weather', 'after', lang_num)}{n} {take_phrase_2('weather', 'days_2', lang_num)}"
    elif n == 7:
        name = take_phrase_2('weather', 'after', lang_num) + take_phrase_2('weather', 'week_0', lang_num)
    
    return name
# TODO exceptions
def get_forecast(message, place, n):
    lang_num = language_define(message)
    name = name_define(n, lang_num)
    
    coords = get_coords(message, place)
    town = coords[0]
    if len(coords) == 3: latitude, longitude = coords[1:]

    if lang_num == 0: town = translate(town, lang_num)
        
    try:  
        weather_inf = get_inf(lang_num, latitude, longitude)
        precipType, summary, search_term, inf = get_main_parts(n, lang_num, town, weather_inf, name)
        bot.send_message(message.chat.id, inf)
    except Exception as e:
        search_term = town
        inf = '' 
        bot.send_message(message.chat.id, take_phrase_2('errors', 'top_error', lang_num))
        report_error(e)
         
    thumbnail_url = get_photo(message, search_term)
    poem = get_poem(message, precipType, summary, search_term)
    
    try:      
        check_user(message)
        check_user_all(message)
        query_add(message, name, town, inf, thumbnail_url, poem)    
    except Exception as e:
        report_error(e) 
    weather_menu(message)
    
def words(lang_num):
    timezone = take_character_2('time_all', 'timezone', lang_num)
    precipType_name = take_character_1('type', lang_num)
    humidity_name = take_character_1('humidity', lang_num)
    wind_name = take_character_2('wind', 'speed', lang_num)
    wind_max_name= take_character_2('wind', 'max', lang_num)
    wind_unit = take_character_2('wind', 'unit', lang_num)
    pressure_name = take_character_2('pressure', 'name', lang_num)
    pressure_unit = take_character_2('pressure', 'unit', lang_num)   
    visibility_name = take_character_2('visibility', 'name', lang_num)
    visibility_unit = take_character_2('visibility', 'unit', lang_num)
    return timezone, precipType_name, humidity_name, wind_name, wind_max_name, wind_unit, pressure_name, pressure_unit, visibility_name, visibility_unit

