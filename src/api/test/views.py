# coding: utf-8
from core.routes import route
from core.webbase import WebHandler
from api.test.validators import TicketAuthorizeValidator, UserAuthorizeValidator


@route(r'/api/common/auth/authorize/$')
class CommonAuthorizeHandler(WebHandler):
    """学生系统验证"""

    def get(self, *args, **kwargs):
        res = 'ok'
        a = self.application
        self.do_success(res)
