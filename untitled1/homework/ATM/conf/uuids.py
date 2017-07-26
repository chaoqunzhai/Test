#_*_coding:utf-8_*_
import os
import json

def uid(func):
    def id():
        path1 = os.path.abspath('..')
        file_path = os.path.join(path1, 'db', 'iddb')
        with open(file_path, 'w', encoding='utf-8') as write_file:
            for i in range(50):
                uuid=6024+i
                write_file.write(json.dumps(uuid) + '\n')
            if uuid > 0:
                func()
    return id