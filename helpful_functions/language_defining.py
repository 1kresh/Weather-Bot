from bot import bot
from dbs.db_filling_main import make_query


def language_define(message):
    ID = message.from_user.id
    lang = make_query('''select Lang from Users_new where Tel_ID=?''', (ID, ))[0][0]
    return 0 if lang == 'English' else 1

