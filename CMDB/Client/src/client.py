from src import plugins
from config import settings
import requests
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
class BaseClient(object):

    def process(self):
        raise NotImplementedError('派生类必须实现process方法')

    def send(self,info):
        # 将资产数据发送到API
        print(settings.API)


        response = requests.post(
            url=settings.API,
            json = info
            # data = info
        )

class AgentClient(BaseClient):

    def process(self):

        info = plugins.server_info()
        self.send(info)

class SubBaseClient(BaseClient):
    def get_host_list(self):
        import json
        response = requests.get(settings.API)
        host_list = json.loads(response.text)
        return host_list
    def task(self,hostname):
        info = plugins.server_info(hostname)
        # 将数据发送到API
        self.send(info)
class SshClient(SubBaseClient):

    def process(self):
        # 获取今日未采集的主机列表 [c1.com,c2.com,c3.com]
        host_list = self.get_host_list()
        pool = ThreadPoolExecutor(10)
        for host in host_list:
            pool.submit(self.task,host)



class SaltClient(SubBaseClient):

    def process(self):
        # 获取今日未采集的主机列表
        host_list = self.get_host_list()
        pool = ThreadPoolExecutor(10)
        for host in host_list:
            pool.submit(self.task,host)