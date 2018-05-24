# coding: utf-8
import hashlib

import requests
import tornado
import tornado.ioloop
from src import conf
from core.webbase import WebHandler


class IndexPageHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self, *args, **kwargs):
        self.render('index.html')


class RegisterPageHandler(WebHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppKey = conf.APP_IM_PROGRAM['APP_KEY']

    def get(self, *args, **kwargs):
        self.render('register.html')

    # def post(self, *args, **kwargs):
    #     current_nonce = '1234sad56789'
    #     current_time = str(int(time.time()))
    #     check_str = self.AppKey + str(current_nonce) + current_time
    #     hash_sha = hashlib.sha1()
    #     hash_sha.update(check_str.encode('utf8'))
    #     print(hash_sha.hexdigest())
    #     headers = {
    #         'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    #         'AppKey': self.AppKey,
    #         'Nonce': current_nonce,
    #         'CurTime': current_time,
    #         'CheckSum': str(hash_sha.hexdigest()),
    #     }
    #     userinfo_dict = {'accid': 'test001', 'name': 'test'}
    #     print(headers)
    #     response = requests.post('https://api.netease.im/nimserver/user/create.action', headers=headers,
    #                              json=userinfo_dict)
    #     print(response.content)
    #     print(response.text)
    #     self.write(response.content)

#
# class WebSocketHandler(tornado.websocket.WebSocketHandler):
#     def check_origin(self, origin):
#         return True
#
#     def open(self):
#         self.write_message(u"Your message was: ")
#
#     def on_message(self, message):
#         self.write_message(u"Your message was: " + message)
#
#     def on_close(self):
#         pass
