from bot import bot
from helpful_functions.language_defining import language_define
from phrases import take_phrase_2
from searching.cvid import cvid

from bs4 import BeautifulSoup
import requests


def get_photo(message, search_term, n=1):
    try:
        req = requests.get(f'http://www.bing.com/images/search?q={search_term}&qs=n&form=QBLH&scope=images&sp=-1&pq={search_term}&sc=8-6&sk=&cvid={cvid}')
        req.encoding = 'cp1251'
        soup = BeautifulSoup(req.text, 'html.parser')
        thumbnail_url = (soup.find_all('img')[n+1]).get('src')
        
        bot.send_photo(message.chat.id, photo=thumbnail_url)
        return thumbnail_url
        
    except Exception as e: 
        lang_num = language_define(message)
        n +=1
        if n==6:
            bot.send_message(message.chat.id, take_phrase_2('errors', 'photo_error', lang_num))
            return ''
        else:
            get_photo(message, search_term, n+1)

