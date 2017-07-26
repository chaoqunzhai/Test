__author__ = 'zhangyao'

class BasePlugin(object):
    """
    - 约束
    - 公共方法
    """

    def __init__(self,host=None):
        self.hostname = host # c1.com

    def agent_cmd(self,cmd):
        """
        本地执行命令
        :param cmd:
        :return:
        """
        # import subprocess
        # v = subprocess.getoutput(cmd)
        # return v
        return 'agent:' + cmd

    def ssh_cmd(self,cmd):
        """
        SSH远程执行命令
        :param cmd:
        :return:
        """
        # import paramiko
        #
        # private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
        #
        # # 创建SSH对象
        # ssh = paramiko.SSHClient()
        # # 允许连接不在know_hosts文件中的主机
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # # 连接服务器
        # ssh.connect(hostname=self.hostname, port=22, username='root', password='123')
        #
        # # 执行命令
        # stdin, stdout, stderr = ssh.exec_command(cmd)
        # # 获取命令结果
        # result = stdout.read()
        #
        # # 关闭连接
        # ssh.close()
        # return result
        return 'ssh:' + cmd
    def salt_cmd(self,cmd):
        # 方式一
        # import subprocess
        # v = subprocess.getoutput('salt %s cmd.run %s' %(self.hostname,cmd,))
        # return v

        # 方式二：
        # vim /usr/bin/salt
        # import salt.client
        # local = salt.client.LocalClient()
        # result = local.cmd(self.hostname, 'cmd.run', [cmd,])
        # return result

        return 'salt:' + cmd

    def cmd(self,c):
        """
        判断当前采集资产是什么模式？根据模式来调用对应的方法获取结果？
        :param cmd:
        :return:
        """
        from config import settings
        if settings.MODE == "Agent":
            result = self.agent_cmd(c)
        elif settings.MODE == "SSH":
            result = self.ssh_cmd(c)
        elif settings.MODE == "Salt":
            result = self.salt_cmd(c)
        else:
            raise Exception('配置文件中Mode设置错误')
        return result

    def execute(self):
        #约束方法, 如果有子类去继承我这个父类，那这里的self 也就是子类本身的。所以子类本身也必须有linux函数，否则就会报父类定义的错误！这就是约束！！！
        return self.linux()

    def linux(self):
        raise NotImplementedError('插件必须实现linux方法')
