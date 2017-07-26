import paramiko



class SSH(object):
    def __init__(self,ip,port,user,passwd):
        self.ip = ip
        self.port = port
        self.user = user
        self.passwd = passwd

        self.transport = None
    def connect(self):
        self.transport = paramiko.Transport((self.ip,self.port))
        self.transport.connect(username=self.user,password=self.passwd)

    def cmd(self,cmd):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin,stdout,stderr = ssh.exec_command(cmd)
        #print(stdout.read())
        return stdout.read()

    def put(self,server_path,local_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path,server_path)
    def get(self,server_path,local_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.get(server_path,local_path)


    def close(self):
        self.transport.close()



obj = SSH('192.168.73.100',22,'root','123456')
obj.connect()
#obj.cmd('df -Th')
print(obj.cmd('df -Th'))
#obj.put()
obj.close()