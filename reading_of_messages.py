from report_error import report_error
from helpful_functions.language_defining import language_define

def choosing(message, _list):
    try:
        if 'открытие' in _list:
            choosing_1(message, _list)
        elif 'закрытие' in _list:
            choosing_2(message, _list)
        else:
            choosing_1(message, _list)
    except Exception as e:
        report_error(e)
        
def choosing_1(message, _list, last_words=None):
    try:
        if 'меню' in _list:
            if 'игра' in _list:
                lang_num = take(message)
                if lang_num == 1:
                    game(message)
            elif 'погода' in _list:
                if 'завтра' in _list:
                    l_w(message, last_words=last_words, time='завтра')   
                elif 'послезавтра' in _list:
                    l_w(message, last_words=last_words, time='послезавра')
                elif 'неделя' in _list:
                    l_w(message, last_words=last_words, time='неделя')
                elif 'сегодня' in _list:
                    l_w(message, last_words=last_words, time='сегодня')
                elif 'сейчас' in _list:
                    l_w(message, last_words=last_words, time='сейчас')
                else:
                    weth_menu(message)
            elif 'статистика' in _list:
                if 'люди' in _list:
                    if 'сегодня' in _list:
                        get_users_today(message) 
                    elif 'все_время' in _list:
                        get_users_all(message)
                    else:
                        l_p(message)
                elif 'запросы' in _list:
                    if 'сегодня' in _list:
                        get_query_today(message) 
                    elif 'все_время' in _list:
                        get_query_all(message)
                    else:
                        l_q(message)
                elif 'рейтинг' in _list:
                    lang_num = take(message)
                    if lang_num == 1:
                        top(message)
                else:
                    stat_menu(message)
            else:
                menu(message)

        elif 'найстройки' in _list:
            if 'язык' in _list:
                if 'рус' in _list:
                    languages_f(message, 'рус')
                elif 'англ' in _list:
                    languages_f(message, 'англ')
                else:
                    languages_set(message)
            elif 'разраб' in _list:
                developing(message)
            else:
                settings(message)
        elif 'погода' in _list:
            if 'завтра' in _list:
                    l_w(message, last_words=last_words, time='завтра')   
            elif 'послезавтра' in _list:
                l_w(message, last_words=last_words, time='послезавра')
            elif 'неделя' in _list:
                l_w(message, last_words=last_words, time='неделя')
            elif 'сегодня' in _list:
                l_w(message, last_words=last_words, time='сегодня')
            elif 'сейчас' in _list:
                l_w(message, last_words=last_words, time='сейчас')
            else:
                weth_menu(message)
        elif 'игра' in _list:
            lang_num = take(message)
            if lang_num == 1:
                game(message)
        elif 'статистика' in _list:
            if 'люди' in _list:
                if 'сегодня' in _list:
                    get_users_today(message)
                elif 'все_время' in _list:
                    get_users_all(message)
                else:
                    l_p(message)
            elif 'запросы' in _list:
                if 'сегодня' in _list:
                    get_query_today(message)
                elif 'все_время' in _list:
                    get_query_all(message)
                else:
                    l_q(message)
            elif 'рейтинг' in _list:
                lang_num = take(message)
                if lang_num == 1:
                    top(message)
            else:
                stat_menu(message)
        elif 'завтра' in _list:
            l_w(message, last_words=last_words, time='завтра')   
        elif 'послезавтра' in _list:
            l_w(message, last_words=last_words, time='послезавра')
        elif 'неделя' in _list:
            l_w(message, last_words=last_words, time='неделя')
        elif 'сегодня' in _list:
            l_w_help(message, last_words)
        elif 'сейчас' in _list:
            l_w(message, last_words=last_words, time='сейчас')
        elif 'язык' in _list:
            if 'рус' in _list:
                languages_f(message, 'рус')
            elif 'англ' in _list:
                languages_f(message, 'англ')
            else:
                languages_set(message)
        elif 'все_время' in _list:
            l_pq(message)
        elif 'разраб' in _list:
            developing(message)
        elif 'запросы' in _list:
            if 'сегодня' in _list:
                get_users_today(message)
            elif 'все_время' in _list:
                get_users_all(message)
            else:
                l_p(message)
        elif 'запросы' in _list:
            if 'сегодня' in _list:
                get_query_today(message)
            elif 'все_время' in _list:
                get_query_all(message)
            else:
                l_q(message)
        elif 'рейтинг' in _list:
            lang_num = take(message)
            if lang_num == 1:
                top(message)     
        elif 'начало' in _list:
            start(message)
        elif 'рус' in _list:
            languages_f(message, 'рус')
        elif 'англ' in _list:
            languages_f(message, 'англ')

        else:
            not_understand(message)
    except Exception as e:
        report_error(e)
        
def choosing_2(message, _list):
    try:
        if 'меню' in _list:
            if 'игра' in _list:
                lang_num = take(message)
                if lang_num == 1:
                    game(message)
            elif 'погода' in _list:
                if 'завтра' in _list:
                    pass
                elif 'послезавтра' in _list:
                    pass
                elif 'неделя' in _list:
                    pass
                elif 'сегодня' in _list:
                    pass
                elif 'сейчас' in _list:
                    pass
                else:
                    pass
            elif 'статистика' in _list:
                if 'люди' in _list:
                    if 'сегодня' in _list:
                        pass
                    elif 'все_время' in _list:
                        pass
                    else:
                        pass
                elif 'запросы' in _list:
                    if 'сегодня' in _list:
                        pass
                    elif 'все_время' in _list:
                        pass
                    else:
                        pass
                else:
                    pass
            else:
                pass


        elif 'найстройки' in _list:
            if 'язык' in _list:
                pass
            elif 'разраб' in _list:
                pass
            else:
                pass
        elif 'погода' in _list:
            if 'завтра' in _list:
                pass
            elif 'послезавтра' in _list:
                pass
            elif 'неделя' in _list:
                pass
            elif 'сегодня' in _list:
                pass
            elif 'сейчас' in _list:
                pass
            else:
                pass
        elif 'игра' in _list:
            pass
        elif 'статистика' in _list:
            if 'люди' in _list:
                if 'сегодня' in _list:
                    pass
                elif 'все_время' in _list:
                    pass
                else:
                    pass
            elif 'запросы' in _list:
                if 'сегодня' in _list:
                    pass
                elif 'все_время' in _list:
                    pass
                else:
                    pass
            else:
                pass
        elif 'завтра' in _list:
            pass  
        elif 'послезавтра' in _list:
            pass
        elif 'неделя' in _list:
            pass
        elif 'сегодня' in _list:
            if 'погода' in _list:
               pass 
            elif 'люди' in _list:
               pass 
            elif 'запросы' in _list:
                pass
            else:
                pass
        elif 'сейчас' in _list:
            pass
        elif 'язык' in _list:
            if 'рус' in _list:
                pass
            elif 'англ' in _list:
                pass
            else:
                pass
        elif 'все_время' in _list:
            pass
        elif 'разраб' in _list:
            pass
        elif 'запросы' in _list:
            if 'сегодня' in _list:
                pass
            elif 'все_время' in _list:
                pass
            else:
                pass 
        elif 'люди' in _list:
            if 'сегодня' in _list:
                pass
            elif 'все_время' in _list:
                pass
            else:
                pass
        elif 'начало' in _list:
            pass
        elif 'рус' in _list:
            pass
        elif 'англ' in _list:
            pass
        else:
            not_understand(message)
    except Exception as e:
        report_error(e)
        
#FIXME обработку слова сегодня 
def l_w(message, time, last_words=None, n=None):
    try:  
        if time == 'сейчас':
            weather(message, ' '.join(last_words))
        else: 
            n = dop_name_reverse(time)
            
        if last_words == None:
            pass
        else:
            pass
    except Exception as e:
        report_error(e)
    
def dop_name_reverse(n):
    if n == 'сегодня':
        name = 0
    elif n == 'завтра':
        name = 1
    elif n == 'послезавтра':
        name = 4
    elif 'неделя':
        name = 7
    return name


        

