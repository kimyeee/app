# coding: utf-8
from core.routes import route
from core.webbase import WebHandler
from api.test.validators import TicketAuthorizeValidator, UserAuthorizeValidator
# from service.stu_system.functions import StuSystemAuthorize
print(11)

@route(r'/api/common/auth/authorize/$')
class CommonAuthorizeHandler(WebHandler):
    """学生系统验证"""

    async def get(self, *args, **kwargs):
        res = 'ok'
        self.do_success(res)

    # async def post(self, *args, **kwargs):
    #     data = self.data
    #     server_type = self.get_param('server_type', 'stu_system')
    #     validator = UserAuthorizeValidator(data)
    #     validated_data = validator.validate()
    #     res = await StuSystemAuthorize.create_ticket(validated_data['user_id'], server_type)
    #     self.do_success(res)
    #
    # async def delete(self, *args, **kwargs):
    #     ticket = self.get_param('ticket')
    #     server_type = self.get_param('server_type', 'stu_system')
    #     validator = TicketAuthorizeValidator({'ticket': ticket}, server_type)
    #     validated_data = validator.validate()
    #     ticket = validated_data['ticket']
    #     await StuSystemAuthorize.delete_ticket(ticket, server_type)
    #     self.do_success()
