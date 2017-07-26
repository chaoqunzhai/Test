import paramiko
import sys
import os
import socket
import select
import threading
from paramiko.py3compat import u

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import setting


try:
    tran = paramiko.Transport((setting.ip,setting.port))
    tran.start_client()
    tran.auth_password(setting.user,setting.passwd)
    # 打开一个通道
    chan = tran.open_session()
    # 获取一个终端
    chan.get_pty()
     # 激活器
    chan.invoke_shell()
except Exception as e:exit('error---')

def connect(chan):
        sys.stdout.write('--------test----')
        while True:
            #readable, writeable, error = select.select([chan, sys.stdin, ], [], [], 1)
            data = u(chan.recv(1024))
            if not data:
                sys.stdout.write('\r\n*** EOF\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data)
            sys.stdout.flush()
t1 = threading.Thread(target=connect,args=(chan,))
t1.start()
try:
    while True:
        d = sys.stdin.read(1)
        if not d:break
        chan.send(d)
except EOFError as e:
    pass
