import socket
import json
import optparse
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DB_HOME = '%s\client\DB' %BASE_DIR
class Client(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s","--server",dest="server",help="server ip")
        parser.add_option("-P", "--port", type='int',dest="port", help="server port")
        self.options,self.args =parser.parse_args()

        self.make_connection()

    def make_connection(self):
        try:
            self.sock = socket.socket()
            self.sock.connect((self.options.server,self.options.port))
        except TypeError as e:
            exit('-h')
    def interactive(self):
        while True:
            choice = input('>>').strip()
            if len(choice) == 0: continue
            if choice == 'q': exit('bay')
            cmd_list = choice.split()
            if hasattr(self, "_%s" % cmd_list[0]):
                func = getattr(self, "_%s" % cmd_list[0])
                func(cmd_list)
            else:pass
    def _put(self,cmd):
        if len(cmd) == 0 or len(cmd) == 1:
            return False
        if os.path.isfile(cmd[1]):
            file_size = os.path.getsize(cmd[1])
            filename = cmd[1].split('/')[-1]
            data_header = {
                "action":'put',
                "filename":filename,
                "filesize":file_size
            }
            self.sock.send(json.dumps(data_header).encode())
            print(data_header)
            #self.sock.recv(1024)
            self.sock.send(b'1')
            with open(cmd[1],'rb') as file:
                 for line in file:
                     self.sock.send(line)
                     #print('111')
        else:
            pass
    def _get(self,cmd):
        os.chdir(DB_HOME)
        if len(cmd) == 0 or len(cmd) == 1:
            return False
        if os.path.isfile(cmd[1]):
            filename = cmd[1].split('/')[-1]
            data_header = {
                "action":'get',
                "filename":filename,
            }
            print(data_header)
            self.sock.send(json.dumps(data_header).encode())
            #self.sock.send(b'1')
            data = self.sock.recv(1024)
            with open(filename,'wb') as file_obj:
                file_obj.write(data)
                file_obj.flush()
                print('yes-----')



if __name__ == '__main__':
    A=Client()
    A.interactive()