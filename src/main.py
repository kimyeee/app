import sys
import tornado.ioloop
import tornado.web
import conf
import tornado.options
import tornado.httpserver
from utils import log as logger
from core.context import TornadoContext


# define("port", default=8008, help="run on th given port", type=int)


class Application(tornado.web.Application):
    def __init__(self, http_port):
        settings = {
            'template_path': r'C:\Users\555\PycharmProjects\ON_app\static',
            'run_mode': conf.RUN_MODE,
            'log_path': conf.LOG_CONFIG.get('path'),
            'log_name': conf.LOG_CONFIG.get('filename'),
            'log_level': conf.LOG_CONFIG.get('level'),
            'mysql_config': conf.MYSQL_CONFIG,
            'handler_pathes': ['api'],
            'http_port': http_port,
            'debug':True
        }
        t_context = TornadoContext(**settings)
        print(t_context.handlers)
        super().__init__(handlers=t_context.handlers, **settings)


def main(port):
    app = Application(port)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port)
    logger.info('Development server is running at http://127.0.0.1:%s/' % port)
    logger.info('start io loop ...')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    port = 8008
    if len(sys.argv) > 1:
        port = sys.argv[1]
    main(port)
