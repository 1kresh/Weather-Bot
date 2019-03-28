from bot import bot
from report_error import report_error
from helpful_functions.language_defining import language_define

from telebot import types

def adding(message):
    try:
        lang_num = take(message)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.row(languages_0('dev_back', lang_num))
        _types = make_query_2('select word from Types')
        _types = [_types[i][0] for i in range(len(_types))]
        bot.send_message(message.chat.id, languages_0('l_types', lang_num)+'\n'+" | ".join(_types), reply_markup=markup)
        adding_01(message)
    except Exception as e:
        report_error(e)
        evolving(message)
def adding_01(message, l=0):
    try:
        lang_num = take(message)
        
        ask_text = languages_0('entering', lang_num)
        sent = bot.reply_to(message, ask_text)
        bot.register_next_step_handler(sent, adding_1)
    except Exception as e:
        report_error(e)
        evolving(message)
        
def adding_1(message):
    try:
        if message.text == 'Back👨🏻‍💻' or message.text == 'Назад👨🏻‍💻':
            evolving(message)
        else:
            lang_num = take(message)
            items = (message.text).strip().split(',')
            item, _type = items[0].strip(), items[1].strip()
            sel = make_query_2('select * from Keys where word=?', (item.lower(), ))
            sel_1 = make_query_2('select * from Keys where type=?', (_type, ))
            if len(sel) == 0:
                make_query_2('''insert into Keys (word, type) values (?, ?)''', (item.lower(), _type, ))
                if len(sel_1) == 0:
                    make_query_2('''insert into Types (word) values (?)''', (_type, ))
                bot.send_message(message.chat.id, 'Слово {} было добавлено в тип {}'.format(item, _type)) 
            else:
                bot.send_message(message.chat.id, 'Слово {} уже было добавлено в тип {}'.format(item, _type))  
            adding(message)
    except Exception as e:
        report_error(e)
        evolving(message)
        
        
def checking(message):
    pass


def deleting_0(message):
    try:
        lang_num = take(message)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.row(languages_0('dev_back', lang_num))
        _types = make_query_2('select word from Types')
        _types = [_types[i][0] for i in range(len(_types))]
        bot.send_message(message.chat.id, languages_0('l_types', lang_num)+ '\n'+' | '.join(_types), reply_markup=markup)
        deleting(message)
    except Exception as e:
        report_error(e)
        evolving(message) 
    
def deleting(message):
    try:
        lang_num = take(message)
        ask_text = '>>>'
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text=languages_0('dev_back', lang_num))
        keyboard.row(button)
        sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
        bot.register_next_step_handler(sent, deleting_1)
    except Exception as e:
        report_error(e)
        evolving(message)
        
def deleting_1(message):
    try:
        if message.text == 'Back👨🏻‍💻' or message.text == 'Назад👨🏻‍💻':
            evolving(message)
        else:
            lang_num = take(message)
            _type = message.text
            make_query_2('DELETE FROM Types WHERE word=?', (_type, ))
            make_query_2('DELETE FROM Keys WHERE type=?', (_type, ))
            bot.send_message(message.chat.id, 'Тип {} был удален'.format(_type))
            evolving(message)
    except Exception as e:
        report_error(e)
        evolving(message)
        
        
def deleting_01(message):
    try:
        lang_num = take(message)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.row(languages_0('dev_back', lang_num))
        words = make_query_2('select word from Keys')
        words = [words[i][0] for i in range(len(words))]
        bot.send_message(message.chat.id, languages_0('l_words', lang_num)+ '\n'+' | '.join(words), reply_markup=markup)
        deleting1(message)
    except Exception as e:
        report_error(e)
        evolving(message) 
    
def deleting1(message):
    try:
        lang_num = take(message)
        ask_text = '>>>'
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text=languages_0('dev_back', lang_num))
        keyboard.row(button)
        sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
        bot.register_next_step_handler(sent, deleting_11)
    except Exception as e:
        report_error(e)
        evolving(message)
        
def deleting_11(message):
    try:
        if message.text == 'Back👨🏻‍💻' or message.text == 'Назад👨🏻‍💻':
            evolving(message)
        else:
            lang_num = take(message)
            word = message.text
            make_query_2('DELETE FROM Keys WHERE word=?', (word, ))
            bot.send_message(message.chat.id, 'Слово {} было удалено'.format(word))
            evolving(message)
    except Exception as e:
        report_error(e)
        evolving(message)

        
def output_0(message):
    try:
        lang_num = take(message)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.row(languages_0('dev_back', lang_num))
        _types = make_query_2('select distinct word from Types')
        _types = [_types[i][0] for i in range(len(_types))]
        bot.send_message(message.chat.id, languages_0('l_types', lang_num)+ '\n'+' | '.join(_types), reply_markup=markup)
        output(message)
    except Exception as e:
        report_error(e)
        evolving(message)
    
def output(message):
    try:
        lang_num = take(message)
        ask_text = '>>>'
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text=languages_0('dev_back', lang_num))
        keyboard.row(button)
        sent = bot.reply_to(message, ask_text, reply_markup = keyboard)
        bot.register_next_step_handler(sent, output_1)
    except Exception as e:
        report_error(e)
        evolving(message)
        
def output_1(message):
    try:
        lang_num = take(message)
        word = message.text
        words = make_query_2('select word from Keys where type=?', (word, ))
        words = [words[i][0] for i in range(len(words))]
        bot.send_message(message.chat.id, languages_0('l_words', lang_num) + '\n'+' | '.join(words))
        evolving(message)
    except Exception as e:
        report_error(e)
        evolving(message)
        
        

