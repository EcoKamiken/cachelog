import pymysql.cursors
from configparser import ConfigParser


class Database():
    config = ConfigParser()
    config.read('cachelog/config/config.ini')

    def __init__(self):
        self.host = self.config['mysql'].get('host')
        self.user = self.config['mysql'].get('user')
        self.port = self.config['mysql'].getint('port')
        self.passwd = self.config['mysql'].get('passwd')
        self.db = self.config['mysql'].get('db')
        self.charset = 'utf8mb4'
        self.cursorclass = pymysql.cursors.DictCursor

    def get_cache_rate(self):
        connection = pymysql.connect(host=self.host,
                                     port=self.port,
                                     user=self.user,
                                     password=self.passwd,
                                     db=self.db,
                                     charset=self.charset,
                                     cursorclass=self.cursorclass)

        with connection.cursor() as cursor:
            sql = """
            SELECT
                (SELECT VARIABLE_VALUE FROM INFORMATION_SCHEMA.GLOBAL_STATUS WHERE VARIABLE_NAME = 'QCACHE_HITS')/(SELECT SUM(VARIABLE_VALUE)
            FROM
                INFORMATION_SCHEMA.GLOBAL_STATUS
            WHERE
                VARIABLE_NAME IN ('QCACHE_HITS','QCACHE_INSERTS','QCACHE_NOT_CACHED'))*100 AS CACHE_HIT_RATE;
            """
            cursor.execute(sql)
            return cursor.fetchone()
