import configparser

import settings
import time

#
# config = configparser.ConfigParser()
# config.read(settings.HOSTS_DIR)
# #config.read(settings.DB_DIR)
# #a=config.sections()
# print(config['mysql']['IP1'])
# print(config.get['mysql']['IP1'])
# for i in config['mysql']:
#     print(i,config['mysql'][i])
# #b=config.options()
# #print(a)
# #print(b)
date=time.strftime('%Y%m%d%M%S')
print(date)