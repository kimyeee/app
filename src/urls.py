# coding:utf-8
from src.api.userinfo.app import *

urls = [
    (r'/ws', WebSocketHandler),
    (r'/register', RegisterPageHandler),
    (r'/', IndexPageHandler),
]
