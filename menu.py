from phrases import (
    take_phrase_1, take_phrase_2)
from helpful_functions.language_defining import language_define
from bot import bot

from telebot import types

def menu(message):
    print(9)
    lang_num = language_define(message)
    menu_text = take_phrase_1('menu_text', lang_num)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(take_phrase_2('quests', 'weather', lang_num), take_phrase_2('quests', 'stats', lang_num))
    if lang_num == 1: markup.row('Игра в города👾')
    markup.row(take_phrase_1('back', lang_num))

    bot.send_message(message.chat.id, menu_text, reply_markup=markup)  