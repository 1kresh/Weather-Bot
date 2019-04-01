from bot import bot
from searching.ei import ei
from report_error import report_error
from helpful_functions.language_defining import language_define
from phrases import take_phrase_2

import requests 
from bs4 import BeautifulSoup

def get_poem(message, precipType, summary, search_term):
    lang_num = language_define(message)
    if lang_num == 1: 
            ways = [[precipType, summary], ['', summary], [precipType, ''], [search_term, '']]
            
            for way in ways:
                try:
                    poem = get_poem_text(message, *way)
                    
                    break
                except:
                    continue
    else:
        poem = ''
    if poem == '':
        bot.send_message(message.chat.id, take_phrase_2('errors', 'poem_error', lang_num))
    return poem
    

def get_poem_text(message, precipType='', summary=''):
    if precipType:
        if summary:
            return poem_request(message, f'{precipType}_{summary}')
        else:
            return poem_request(message, precipType)

    elif summary:
        if "облач" in summary.lower() or "cloud" in summary.lower(): 
            summary = 'облачно'
        elif 'солн' in summary.lower() or 'sun' in summary.lower():
            summary = 'солнечно'
        elif 'дожд' in summary.lower() or 'rain' in summary.lower():
            summary = 'дождливо'
        
        poem = poem_request(message, '+'.join(summary.strip().split()))
        return poem
    else:
        return ''
            
def poem_request(message, name, n=0):
    
    req = requests.get(f'https://www.google.ru/search?newwindow=1&source=hp&ei={ei}&btnG=Поиск&q={name}+site%3Astihi.ru')
    if req.status_code == 200:
        req.encoding = 'cp1251'
        soup = BeautifulSoup(req.text, 'html.parser')
        for n in range(6):
            href = (soup.find_all('a')[26+n]).get('href')
            l = href.find('q=')
            r = href.find('&')
            url = href[l+2:r]
            req = requests.get(url).text
            soup = BeautifulSoup(req, 'html.parser')
            poem = soup.find_all('div')[6].text
            poem = poem.replace(u'\xa0', u' ')
            if poem != '' and 'перенесено' not in poem and 'Написать личное сообщение' not in poem:
                bot.send_message(message.chat.id, poem)
                break
        return poem
    else:
        raise Exception
 

