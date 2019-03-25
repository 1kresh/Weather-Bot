import datetime

def date_time(obj='all'):
    datetime_utc3 = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
    if obj == 'all':
        return str(datetime_utc3.date()), str(datetime_utc3.time().strftime('%H:%M:%S'))
    elif obj == 'date':
        return str(datetime_utc3.date())
    elif obj == 'time':
        return str(datetime_utc3.time().strftime('%H:%M:%S'))