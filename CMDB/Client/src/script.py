__author__ = 'zhangyao'
from config import settings
from src import client
def run():
    if settings.MODE == 'Agent':
        obj = client.AgentClient()
    elif settings.MODE == 'SSH':
        obj = client.SshClient()
    elif settings.MODE == 'Salt':
        obj = client.SaltClient()
    else:
        raise Exception('....')
    obj.process()
