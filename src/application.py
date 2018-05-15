from src.core.context import TornadoContext
import tornado.web
from src import conf


class Application(tornado.web.Application):
    def __init__(self):
        print(conf)
        settings = {
            # "static_path": r"C:\Users\555\PycharmProjects\static",
            'template_path': r'C:\Users\555\PycharmProjects\ON_app\static',
            'run_mode': conf.RUN_MODE,
            'log_level': conf.LOG_CONFIG.get('level'),
            'log_path': conf.LOG_CONFIG.get('path'),
            'log_name': conf.LOG_CONFIG.get('filename'),
            'mysql_config': conf.MYSQL_CONFIG,
            'handler_pathes': ['core'],
        }
        t_context = TornadoContext(**settings)
        super().__init__(handlers=t_context.handlers, **settings)
