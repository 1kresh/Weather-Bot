from bot import bot
from helpful_functions.language_defining import language_define
from phrases import (
    take_phrase_1, take_phrase_2)

from telebot import types


def stat_menu(message):
    lang_num = language_define(message)
    text = take_phrase_2('statistic', 'stats_text', lang_num)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(take_phrase_2('statistic', 'today_users', lang_num), take_phrase_2('statistic', 'all_users', lang_num))
    markup.row(take_phrase_2('statistic', 'today_requests', lang_num), take_phrase_2('statistic', 'all_requests', lang_num))
    if lang_num == 1:
        markup.row('Рейтинг игроков🏆')
    markup.row(take_phrase_1('back_menu', lang_num), take_phrase_1('back_start', lang_num))
    bot.send_message(message.chat.id, text, reply_markup=markup)