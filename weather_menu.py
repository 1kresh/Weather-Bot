from bot import bot
from helpful_functions.language_defining import language_define
from phrases import (
    take_phrase_1, take_phrase_2)

from telebot import types


def weather_menu(message):
    lang_num = language_define(message)
    text = take_phrase_2('weather', 'weather_text', lang_num)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(take_phrase_2('weather', 'now', lang_num), take_phrase_2('weather', 'today', lang_num))
    markup.row(take_phrase_2('weather', 'tomorrow', lang_num), take_phrase_2('weather', 'day_after_tomorrow', lang_num))
    markup.row(take_phrase_2('weather', 'week', lang_num))
    markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))

    bot.send_message(message.chat.id, text, reply_markup=markup)    