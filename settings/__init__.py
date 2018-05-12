try:
    from settings.prod import *
except ImportError:
    try:
        from settings.test import *
    except ImportError:
        from settings.dev import *