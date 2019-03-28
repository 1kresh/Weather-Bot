from report_error import report_error
from dbs.db_filling_main import make_query

def prepare_db():
    try:
        make_query("CREATE TABLE IF NOT EXISTS Users_All (Ua_ID INTEGER PRIMARY KEY AUTOINCREMENT, FirstName text, LastName text, Tel_ID INTEGER, Username text, Time date);")
        make_query("CREATE TABLE IF NOT EXISTS Users (U_ID INTEGER PRIMARY KEY AUTOINCREMENT, FirstName text, LastName text, Tel_ID INTEGER, Username text);")
        make_query("CREATE TABLE IF NOT EXISTS Users_All_new (Ua_ID INTEGER PRIMARY KEY AUTOINCREMENT, FirstName text, LastName text, Tel_ID text, Username text, Time date, Lang text);")
        make_query("CREATE TABLE IF NOT EXISTS Users_new (U_ID INTEGER PRIMARY KEY AUTOINCREMENT, FirstName text, LastName text, Tel_ID text, Username text, Lang text);")
        make_query("CREATE TABLE IF NOT EXISTS Queries (Q_ID INTEGER PRIMARY KEY AUTOINCREMENT, Quest text, Town TEXT, Weather TEXT, Photo TEXT, Poem text, Tel_ID integer, Time_d date, Time text);")
        make_query("CREATE TABLE IF NOT EXISTS Queries_stat (Qs_ID INTEGER PRIMARY KEY AUTOINCREMENT, Statistic text, Answer TEXT, Tel_ID integer, Time_d date, Time text);")
        make_query("CREATE TABLE IF NOT EXISTS Translations (U_ID INTEGER PRIMARY KEY AUTOINCREMENT, main text, sub text, num integer);")
        make_query("CREATE TABLE IF NOT EXISTS Rus_Towns (Russian text);")
        make_query("CREATE TABLE IF NOT EXISTS Inf_towns (U_ID INTEGER PRIMARY KEY AUTOINCREMENT, town text, inf text);")
        make_query("CREATE TABLE IF NOT EXISTS Winners (Ua_ID INTEGER PRIMARY KEY AUTOINCREMENT, Name text);")
    except Exception as e:
        report_error(e)

