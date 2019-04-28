from report_error import report_error

import sqlite3


def make_query(*params):
    try:
        conn = sqlite3.connect('Base.db')
        c = conn.cursor()
        c.execute(*params)
        retur = c.fetchall()
        conn.commit()
        conn.close()
        return retur
    except Exception as e:
        report_error(e)

