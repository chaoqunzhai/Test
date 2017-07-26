import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
import logging
"""
def error_log(message):
    #创建文件对象
    file_1_1 = logging.FileHandler('error.log', 'a+', encoding='utf-8')
    fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
    file_1_1.setFormatter(fmt)
    # 创建日志对象
    logger1 = logging.Logger('error', level=logging.ERROR)

    # 日志对象和文件对象创建关系
    logger1.addHandler(file_1_1)

    logger1.log(logging.FATAL,message)

def run_log(message):
    file_1_1 = logging.FileHandler('run.log', 'a+', encoding='utf-8')
    fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
    file_1_1.setFormatter(fmt)
    # 创建日志对象
    logger1 = logging.Logger('run', level=logging.ERROR)
    # 日志对象和文件对象创建关系
    logger1.addHandler(file_1_1)

    logger1.log(logging.FATAL,message)
"""

class LoggerHelper(object):
    _i = None

    @classmethod
    def instance(cls):
        if cls._i:
            return cls._i
        else:
            cls._i = LoggerHelper() #LoggerHelper()
            return cls._i # obj

    def __init__(self):
        #创建文件对象
        error_log = logging.FileHandler('error.log', 'a+', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        error_log.setFormatter(fmt)
        # 创建日志对象
        error_logger = logging.Logger('error', level=logging.ERROR)
        # 日志对象和文件对象创建关系
        error_logger.addHandler(error_log)
        self.error_logger = error_logger

        # 创建文件对象
        run_log = logging.FileHandler('run.log', 'a+', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        run_log.setFormatter(fmt)
        # 创建日志对象
        run_logger = logging.Logger('run', level=logging.ERROR)
        # 日志对象和文件对象创建关系
        run_logger.addHandler(run_log)
        self.run_logger = run_logger


if __name__ == '__main__':

    # 单例模式，用户获得第一次创建的对象
    obj1 = LoggerHelper.instance()
    obj1.error_logger.log(logging.FATAL,'a1')

    obj2 = LoggerHelper.instance()
    obj2.run_logger.log(logging.FATAL,'a2')

    obj3 = LoggerHelper.instance()
    obj3.run_logger.log(logging.FATAL,'a3')












