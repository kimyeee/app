try:
    from conf.prod import *
except ImportError:
    from conf.dev import *
    from conf.common import *