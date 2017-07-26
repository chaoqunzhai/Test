__author__ = 'zhangyao'
import traceback
from .base import BasePlugin
from lib.response import BaseResponse
from lib.logger_helper import LoggerHelper

class DiskPlugin(BasePlugin):
    def linux(self):
        """
        执行命令，获取资产信息
        :return:
        """
        # ret = {'status': True,'data': None,'error': None}
        ret = BaseResponse()  #采用封装对象的方法，，实现可扩展
        try:
            result = self.cmd('disk')
            # ret['data'] = result
            ret.data = result
        except Exception as e:
            # ret['status'] = False
            # ret['error'] = traceback.format_exc()
            v = traceback.format_exc()
            ret.status = False
            ret.error = v
            # 写入本地日志
            # 写入本地日志
            obj = LoggerHelper.instance()
            obj.error_logger.log(50,v)


        return ret