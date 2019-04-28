from dbs.db_filling_main import make_query
from helpful_functions.translation_key import translation_key
from report_error import report_error

import json
import requests


def translate(to_translate, lang_num=1):
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
            
        return translated
    except Exception as e:
        report_error(e)

