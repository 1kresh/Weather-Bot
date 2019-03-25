from report_error import report_error

import sqlite3

def make_query(*params):
    print(29)
    try:
        conn = sqlite3.connect('DBs\Корохов_Андрей.db')
        c = conn.cursor()
        c.execute(*params)
        retur = c.fetchall()
        conn.commit()
        conn.close()
        return retur
    except Exception as e:
        report_error(e)

def make_query_1(*params):
    print(30)
    try:
        conn = sqlite3.connect('DBs\Towns_id.db')
        c = conn.cursor()
        c.execute(*params)
        retur = c.fetchall()
        conn.commit()
        conn.close()
        return retur
    except Exception as e:
        report_error(e)
    
def make_query_2(*params):
    print(31)
    try:
        conn = sqlite3.connect('DBs\M_L.db')
        c = conn.cursor()
        c.execute(*params)
        retur = c.fetchall()
        conn.commit()
        conn.close()
        return retur
    except Exception as e:
        report_error(e)

