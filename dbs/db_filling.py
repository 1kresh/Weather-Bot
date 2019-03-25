from report_error import report_error
from dbs.db_filling_main import make_query
from helpful_functions.date_time_defining import date_time

def query_add(message, quest, town, inf, thumbnail_url, poem):
    print(23)
    try:
        Quest = quest
        Town = town
        Weather = inf
        Photo = thumbnail_url
        Poem = poem
        Tel_ID = message.from_user.id
        Time_d, Time = date_time()

        make_query('''insert into Queries (Quest, Town, Weather, Photo, Poem, Tel_ID, Time_d, Time ) 
        values (?, ?, ?, ?, ?, ?, ?, ?)''', (Quest, Town, Weather, Photo, Poem, Tel_ID, Time_d, Time))
    except Exception as e:
        report_error(e)

def query_add_stat(message, stat, answer):
    print(24)
    try:
        Statistic = stat
        Answer = answer
        Tel_ID = message.from_user.id
        Time_d, Time = date_time()

        make_query('''insert into Queries_stat (Statistic, Answer, Tel_ID, Time_d, Time) 
        values (?, ?, ?, ?, ?)''', (Statistic, Answer, Tel_ID, Time_d, Time))
    except Exception as e:
        report_error(e)

def check_user(message):
    print(25)
    try:
        FirstName = message.from_user.first_name
        LastName = message.from_user.last_name
        Tel_ID = message.from_user.id
        Username = message.from_user.username

        if(len(make_query('''select * from Users where Tel_ID = ? ''', (Tel_ID, ))) == 0):
            make_query('''insert into Users (FirstName, LastName, Tel_ID, Username) 
            values (?, ?, ?, ?)''', (FirstName, LastName, Tel_ID, Username, ))
    except Exception as e:
        report_error(e)
        
def check_user_all(message):
    print(26)
    try:
        FirstName = message.from_user.first_name
        LastName = message.from_user.last_name
        Tel_ID = message.from_user.id
        Username = message.from_user.username
        Time_d, Time = date_time()

        make_query('''insert into Users_All_new (FirstName, LastName, Tel_ID, Username, Time) 
        values (?, ?, ?, ?, ?)''', (FirstName, LastName, Tel_ID, Username, Time))
    except Exception as e:
        report_error(e)
        
def check_user_new(message, lang):
    print(27)
    try:
        FirstName = message.from_user.first_name
        LastName = message.from_user.last_name
        Tel_ID = str(message.from_user.id)
        Username = message.from_user.username

        if(len(make_query('''select * from Users_new where Tel_ID = ? ''', (Tel_ID, ))) == 0):
            make_query('''insert into Users_new (FirstName, LastName, Tel_ID, Username, Lang) 
            values (?, ?, ?, ?, ?)''', (FirstName, LastName, Tel_ID, Username, lang, ))
    except Exception as e:
        report_error(e)

def check_user_all_new(message, lang):
    print(28)
    try:
        FirstName = message.from_user.first_name
        LastName = message.from_user.last_name
        Tel_ID = str(message.from_user.id)
        Username = message.from_user.username
        Time_d, Time = date_time()

        make_query('''insert into Users_All_new (FirstName, LastName, Tel_ID, Username, Time, Lang) 
        values (?, ?, ?, ?, ?, ?)''', (FirstName, LastName, Tel_ID, Username, Time, lang))
    except Exception as e:
        report_error(e)
        

