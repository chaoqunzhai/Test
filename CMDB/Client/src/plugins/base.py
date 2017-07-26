
class BasePlugin(object):
    '''
    约束
    公共方法
    '''
    def __init__(self,host=None):
        self.hostname = host
    def execute(self):
        #在这判断系统
         self.linux()
    def shell_cmd(self,cmd):
        import subprocess
        v = subprocess.getoutput(cmd)
        return v
    def ssh_cmd(self,cmd):
        """
        SSH远程执行命令
        :param cmd:
        :return:
        """
        import paramiko

        private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=self.hostname, port=22, username='root', password='123')

        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 获取命令结果
        result = stdout.read()

        # 关闭连接
        ssh.close()
        return result
        # return 'ssh:' + cmd

    def salt_cmd(self,cmd):
        import salt.client


    def cmd(self,cmd):
        '''
        #判断如果是什么模式,根据模式来调用对应的方法获取结果
        :param cmd:
        :return:
        '''
        from config import settings
        if settings.MODE == "Agent":
            result = self.shell_cmd(cmd)
        elif settings.MODE == "SSH":
            result = self.ssh_cmd(cmd)
        elif settings.MODE == "Salt":
            result = self.salt_cmd(cmd)
        else:
            raise Exception('配置文件中Mode设置错误')
        return result
    def linux(self):

        raise NotImplementedError('插件必须实现linux方法')

    def windows(self):

        raise NotImplementedError('插件必须实现windows方法')



