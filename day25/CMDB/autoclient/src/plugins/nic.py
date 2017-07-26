__author__ = 'zhangyao'
import traceback
from .base import BasePlugin
from lib.response import BaseResponse
from lib.logger_helper import LoggerHelper
class NicPlugin(BasePlugin):
    def linux(self):
        """
        执行命令，获取资产信息
        :return:
        """
        ret = BaseResponse()
        try:
            result = self.cmd('nic')
            ret.data = result
        except Exception as e:
            v = traceback.format_exc()
            ret.status = False
            ret.error = v
            # 写入本地日志
            obj = LoggerHelper.instance()
            obj.error_logger.log(50,v)
        return ret