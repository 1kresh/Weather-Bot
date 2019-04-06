from bot import bot
from report_error import report_error
import datetime
from phrases import (
    phrases, take_phrase_2)
from dbs.db_filling_main import make_query
from dbs.db_filling import (
    query_add_stat, check_user, check_user_all)
from helpful_functions.language_defining import language_define
from helpful_functions.date_time_defining import date_time

def get_query_today(message):
    try:
        lang_num = language_define(message)
        Time_d = date_time('date')
        queries = (make_query('''select count(*) from (select * from Queries where Time_d=?); ''', (Time_d, )))[0][0]
        queries_s = (make_query('''select count(*) from (select * from Queries_stat where Time_d=?); ''', (Time_d, )))[0][0]
        answer = take_phrase_2('stat_answers', 'requests_today', lang_num)+str(queries+queries_s)
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        report_error(e)
    try:
        query_add_stat(message, phrases['stat_db']['requests_today'], answer)
        check_user(message)
        check_user_all(message)
    except Exception as e:
        report_error(e)
        
def get_query_all(message): 
    try:
        lang_num = language_define(message)
        queries = (make_query('''select count(*) from (select * from Queries); '''))[0][0]
        queries_s = (make_query('''select count(*) from (select * from Queries_stat);'''))[0][0]

        answer = f"{take_phrase_2('stat_answers', 'requests_all', lang_num)}{queries+queries_s}"
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        report_error(e)
    try:
        query_add_stat(message, phrases['stat_db']['requests_all'], answer)
        check_user(message)
        check_user_all(message)
    except Exception as e:
        report_error(e)

