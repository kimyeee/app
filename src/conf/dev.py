# coding: utf-8
import pymysql

RUN_MODE = 'console'

MYSQL_CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'on_app',
    'user': 'root',
    'password': '123456',
    'cursorclass': pymysql.cursors.DictCursor,
    'charset': 'utf8'
}


REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379
}