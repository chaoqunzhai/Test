import logging

class LoggerHelper(object):
    _i = None
    @classmethod
    def instance(cls):
        if cls._i:
            return cls._i
        else:
            cls._i = LoggerHelper()
            return cls._i

    def __init__(self):
        error_log = logging.FileHandler('error.log', 'a+', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        error_log.setFormatter(fmt)
        # 创建日志对象
        error_logger = logging.Logger('error', level=logging.ERROR)
        # 日志对象和文件对象创建关系
        error_logger.addHandler(error_log)
        self.error_logger = error_logger

        run_log = logging.FileHandler('run.log', 'a+', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        run_log.setFormatter(fmt)
        # 创建日志对象
        run_logger = logging.Logger('run', level=logging.ERROR)
        # 日志对象和文件对象创建关系
        run_logger.addHandler(run_log)
        self.run_logger = run_logger
# if __name__ == '__main__':
#
#     # 单例模式，用户获得永远是第一次创建的对象
#     ##内部只会运行一次
#     obj1 = LoggerHelper.instance()
#     obj1.run_logger.log(logging.FATAL,'asdfasdfasdfasdf')
#
#     obj2 = LoggerHelper.instance()
#     obj2.run_logger.log(logging.FATAL,'asdfasdfasdfasdf')
#
#     obj3 = LoggerHelper.instance()
#     obj3.run_logger.log(logging.FATAL,'asdfasdfasdfasdf')