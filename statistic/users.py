from bot import bot
from report_error import report_error
import datetime
from dbs.db_filling_main import make_query
from phrases import take_phrase_2
from dbs.db_filling import (
    query_add_stat, check_user, check_user_all)
from helpful_functions.language_defining import language_define
from helpful_functions.date_time_defining import date_time
def get_users_today(message):
    try:
        lang_num = language_define(message)
        Time_d = date_time('date')
        #print(make_query('select * from Users_All_new'))
        
        queries = [make_query(f'''select distinct Tel_ID from Users_All where Time = {Time_d}; '''), 
                 make_query(f'''select distinct Tel_ID from Users_All_new where Time = {Time_d}; ''')]
        
        people = set()
        for query in queries:
            for user in query:
                people.add(user[0])
        
        answer = f"{take_phrase_2('stat_answers', 'users_today', lang_num)}{len(people)}"
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        report_error(e) 
    try:
        query_add_stat(message, take_phrase_2('stat_db', 'users_today', 0), answer)
        check_user(message)
        check_user_all(message)
    except Exception as e:
        report_error(e)
        
def get_users_all(message):   
    try:
        lang_num = language_define(message)
        queries = [make_query('''select Tel_ID from Users'''), make_query('''select Tel_ID from Users_new''')]
        
        people = set()
        for query in queries:
            for user in query:
                people.add(user[0])
                    
        answer = f"{take_phrase_2('stat_answers', 'users_all', lang_num)}{len(people)}"
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        report_error(e)
    try:
        query_add_stat(message, take_phrase_2('stat_db', 'users_all', 0), answer)
        check_user(message)
        check_user_all(message)
    except Exception as e:
        report_error(e)

