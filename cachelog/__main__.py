import datetime
import cachelog.database

obj = cachelog.database.Database()
rate = obj.get_cache_rate()
dt = datetime.datetime.now()
today = dt.strftime('%Y/%m/%d, ')

filename = 'cachelog/log/log.csv'
with open(filename, 'a', newline='\n') as fp:
    fp.writelines(today + str(rate['CACHE_HIT_RATE']) + '\n')
