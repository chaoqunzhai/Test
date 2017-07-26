import paramiko


ssh = paramiko.SSHClient()

#设置主机不在khost_key中也能连接
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.12.100',port=22,username='root',password='123456')

stdin,stdout,stderror =  ssh.exec_command('df -Th')

print(stdout.read())