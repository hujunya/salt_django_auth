import ConfigParser

try:
    config = ConfigParser.ConfigParser()
    config.read('/opt/projects/configs/server.conf')
    ENV = config.get('global', 'env')
except:
    ENV = 'dev'

if ENV == 'prod':
    from .prod import *
elif ENV == 'test':
    from .test import *
else:
    from .dev import *
