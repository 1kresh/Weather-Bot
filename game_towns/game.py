from bot import bot
from phrases import take_phrase_1, take_game_phrase
from menu import menu
from dbs.db_filling_main import make_query
from telebot import types
import random

def nickname_define(message):

    name, surname = message.from_user.first_name, message.from_user.last_name
    if name:
        nickname = f'{surname}_{name}' if surname else name
    else:
        nickname = surname if surname else 'Somebody'
        
    return nickname
    
def prepare_game_db(message):
    print(33)
    try:
        nickname = nickname_define(message)
        make_query("DROP TABLE IF EXISTS {};".format(nickname))
        make_query("CREATE TABLE {} (Ua_ID INTEGER PRIMARY KEY AUTOINCREMENT, Town text);".format(nickname))
    except Exception as e:
        report_error(e)

def preparing_game(message, state=1):
    if state == 1:
        prepare_game_db(message)
        text = take_game_phrase('glhf')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(take_phrase_1('back_menu', 1), take_phrase_1('back_start', 1))
        bot.send_message(message.chat.id, text, reply_markup=markup) 
        text = take_game_phrase('write_town')
    else:
        text = take_game_phrase('write_other_town')

    sent = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent, game_play)
    
def game_play(message):
    place = message.text

    if place == take_phrase_1('back_menu',1):
        menu(message)

    towns = (make_query('''select Russian from Rus_Towns; ''')[0][0]).split()
    towns = [town.lower() for town in towns]
    place = place.lower()

    if place in towns:
        nickname = nickname_define(message)
        forbidden_letters = ('ё', 'ъ', 'ь', 'ы')
        choice = list()

        make_query(f'insert into {nickname} (Town) values (?)', (place, ))
        #print(nickname, make_query_1('select * from {}'.format(nickname)))
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in [take_game_phrase('inf')]])
        
        bot.send_message(message.chat.id, take_game_phrase('town_inf').format(place), reply_markup=keyboard)

        for i in range(1, 4):
            if place[-i] not in forbidden_letters:
                sym = place[-i]
                break

        for town in towns:
            if sym == town[0] and town != place:
                choice.append(town)
        random_town = random.choice(choice)

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in [take_game_phrase('inf')]])
        bot.send_message(message.chat.id, random_town, reply_markup=keyboard)

        make_query(f'insert into {nickname} (Town) values (?)', (random_town, ))

        preparing_game_1(message, random_town, towns, forbidden_letters)
                
    else:
        preparing_game(message, 0)
        
def preparing_game_1(message, place, towns, forbidden_letters, state=0):
    for i in range(1, 4):
        if place[-i] not in forbidden_letters:
            sym = place[-i]
            break

    nickname = nickname_define(message)       
    used_towns = make_query(f'''select Town from {nickname}; ''')
    used_towns = [town[0].lower() for town in used_towns]
    choice = list()

    for town in towns:
        if sym == town[0] and town not in used_towns: 
            choice.append(town)

    if len(choice) == 0:
        defeat(message, sym)
        menu(message)
    else: 
        sym = sym.upper()
        if state == 0:
            ask_text = take_game_phrase('write_town_with_letter').format(sym)
        elif state == 1:
            ask_text = take_game_phrase('write_other_town_with_letter').format(sym)
        else:
            ask_text = take_game_phrase('write_town_with_other_letter').format(sym)

        sent = bot.send_message(message.chat.id, ask_text)
        bot.register_next_step_handler(sent, game_play_1)
        
    
def game_play_1(message):
    place = message.text

    if place == take_phrase_1('back_menu',1):
        menu(message)
        
    towns = (make_query('''select Russian from Rus_Towns; ''')[0][0]).split()
    towns = [town.lower() for town in towns]
    nickname = nickname_define(message)
    used_towns = make_query(f'''select Town from {nickname}; ''')
    used_towns = [town[0].lower() for town in used_towns]
    place = place.lower()
    
    if place in towns and place not in used_towns:
        forbidden_letters = ('ё', 'ъ', 'ь', 'ы')
        last_town = used_towns[-1][0]
        choice = list()
        
        for i in range(1, 4):
            if last_town[-i] not in forbidden_letters:
                bot_sym = last_town[-i]
                break

        if bot_sym == place[0]:
            
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in [take_game_phrase('inf')]])
            bot.send_message(message.chat.id, take_game_phrase('town_inf').format(place), reply_markup=keyboard)
            make_query(f'insert into {nickname} (Town) values (?)', (place, ))
            
            if len(used_towns) == 20:
                finish(message, nickname)
            else:
                for i in range(1, 4):
                    if place[-i] not in forbidden_letters:
                        user_sym = place[-i]
                        break
                for town in towns:
                    if user_sym == town[0] and town not in used_towns: 
                        choice.append(town)
 
                if len(choice) == 0:
                    finish(message, nickname, user_sym)
                else:
                    random_town = random.choice(choice)

                    keyboard = types.InlineKeyboardMarkup()
                    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in [take_game_phrase('inf')]])
                    bot.send_message(message.chat.id, random_town, reply_markup=keyboard)

                    make_query(f'insert into {nickname} (Town) values (?)', (random_town, ))
                    preparing_game_1(message, random_town, towns, forbidden_letters)

        else:
            preparing_game_1(message, used_towns[-1], towns, forbidden_letters, state=2)
    else:
        preparing_game_1(message, used_towns[-1], towns, forbidden_letters, state=1)
        
        

def finish(message, nickname, letter=None):
    if letter:
        cong_text = take_game_phrase('congrats_letter').format(letter.upper())
    else:
        cong_text = take_game_phrase('congrats')

    bot.send_message(message.chat.id, cong_text, parse_mode='Markdown')
    make_query('insert into Winners (Name) values (?)', (nickname, ))
    menu(message)

def defeat(message, letter):
    bot.send_message(message.chat.id, take_game_phrase('defeat').format(letter), parse_mode='Markdown')
    menu(message)
    
    

