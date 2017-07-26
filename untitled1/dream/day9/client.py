import socket

import os
import json
client = socket.socket()

client.connect(('localhost',9000))


while True:
    choirce = input('>>').strip()
    if  len(choirce) == 0 :continue
    cmd_list = choirce.split()

    if cmd_list[0] == 'put':
        if len(cmd_list) == 1:
            print('no findname ')
            continue
        filename = cmd_list[1]
        if os.path.isfile(filename):
            file_obj = open(filename,'rb')
            base_filename = filename.split("/")[-1]           #以/来切分， 取最后一个，也就是文件名字
            print(file_obj.name,os.path.getsize(filename))
            data_header = {
                "action":'put',
                "filename":base_filename,
                "size":os.path.getsize(filename)
            }
            client.send(json.dumps(data_header).encode())        #发送 data_header字典 ，server端可以通过字典获取方式
            for lien in file_obj:
                client.send(lien)
            print('---send file done -----')


        else:
            print('file is not valid')
            continue
    elif cmd_list[0] == 'get':
        pass