import pymysql.cursors
from configparser import ConfigParser


class Database():
    config = ConfigParser()
    config.read('config/config.ini')

    def __init__(self):
        self.host = self.config['mysql'].get('host')
        self.user = self.config['mysql'].get('user')
        self.port = self.config['mysql'].getint('port')
        self.passwd = self.config['mysql'].get('passwd')
        self.db = self.config['mysql'].get('db')
        self.charset = 'utf8mb4'
        self.cursorclass = pymysql.cursors.DictCursor
