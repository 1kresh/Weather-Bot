from helpful_functions.translation_key import translation_key
from report_error import report_error
from dbs.db_filling_main import make_query

import requests
import json

def translate(to_translate, lang_num=1):
    print(21)
    try:
        trans = make_query('select * from Translations where main=? or sub=?', (to_translate, to_translate, ))
        try: 
            translated = tran[0 if tran[0][3] == lang_num else 1][2] 
        except:
            data = {"key": translation_key, 
                    "text": to_translate,
                    "lang": "ru" if lang_num == 1 else "en"}

            req_data = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', data=data).json()
            translated = req_data['text'][0]

            #make_query('insert into Translations (main, sub, num) values (?, ?, ?)', (to_translate, translated, lang_num, ))
            #make_query('insert into Translations (main, sub, num) values (?, ?, ?)', (translated, to_translate, abs(lang_num-1), ))
            
        return translated
    except Exception as e:
        report_error(e)

