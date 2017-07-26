__author__ = 'zhangyao'

"""
import traceback
try:
    int('asdf')
except Exception as e:
    # print(e)
    print(traceback.format_exc())
"""

import logging


"""
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
"""

# 只能写入到一个文件，多次声明无效
# logging.basicConfig(
#     filename='l1.log',
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level=logging.INFO
# )
# logging.log(logging.ERROR,'123123')


# 定义文件
# file_1_1 = logging.FileHandler('l1_1.log', 'a+', encoding='utf-8')
# fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
# file_1_1.setFormatter(fmt)
#
# # 定义操作文件的对象2
# file_1_2 = logging.FileHandler('l1_2.log', 'a+', encoding='utf-8')
# fmt = logging.Formatter(fmt="%(asctime)s:  %(message)s")
# file_1_2.setFormatter(fmt)
#
# # 创建日志对象
# logger1 = logging.Logger('lilai', level=logging.ERROR)
# # 日志对象和文件对象创建关系
# logger1.addHandler(file_1_1)
# logger1.addHandler(file_1_2)
#
# logger1.log(logging.FATAL,'asdfasdfasdf')




# 定义操作文件的对象2
# file_1_2 = logging.FileHandler('l1_2.log', 'a', encoding='utf-8')
# fmt = logging.Formatter()
# file_1_2.setFormatter(fmt)

# 定义日志
# logger1 = logging.Logger('lilai', level=logging.ERROR)
# logger1.addHandler(file_1_1)
# logger1.addHandler(file_1_2)


# 写日志
# logger1.critical('1111')



# from lib import logger_helper
#
# logger_helper.error_log('asdfasdfasdf')
# logger_helper.error_log('fff')
# logger_helper.run_log('fff')






















