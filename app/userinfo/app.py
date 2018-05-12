# coding: utf-8
import hashlib

import requests
import time
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

from settings.common import APP_IM_PROGRAM


class IndexPageHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self, *args, **kwargs):
        self.render('index.html')


class RegisterPageHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.AppKey = APP_IM_PROGRAM['APP_KEY']
        self.hash_sha = hashlib.sha1()

    def get(self, *args, **kwargs):
        self.render('register.html')

    def post(self, *args, **kwargs):
        current_nonce = 123456789
        check_str = self.AppKey + str(current_nonce) + str(time.time())
        check_sum = self.hash_sha.update(check_str.encode('utf8'))
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
            'AppKey': self.AppKey,
            'Nonce': current_nonce,
            'CurTime': time.time(),
            'CheckSum': check_sum,
        }
        userinfo_dict = {'accid': 'test001', 'name': 'test'}
        response = requests.post('https://api.netease.im/nimserver/user/create.action', headers=headers,
                                 json=userinfo_dict)
        print(response.content)
        print(response.text)
        self.write(response.content)


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        self.write_message(u"Your message was: ")

    def on_message(self, message):
        self.write_message(u"Your message was: " + message)

    def on_close(self):
        pass


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/ws', WebSocketHandler),
            (r'/register', RegisterPageHandler),
            (r'/', IndexPageHandler),
        ]
        settings = {"static_path": r"C:\Users\555\PycharmProjects\static"}
        super().__init__(handlers, **settings)


if __name__ == '__main__':
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
