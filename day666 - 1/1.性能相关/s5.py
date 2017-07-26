"""
目标：单线程实现并发Http请求
socket
IO多路复用
Http协议

流程：
    http://www.cnblogs.com/wupeiqi/articles/6229292.html
    1. sk 连接，IP和端口进行连接 www.cnblogs.com
    2. 请求信息
        请求头：
            k=v\r\n
            k=v\r\n
            k=v\r\n
            \r\n\r\n
            请求体
        sk.sendall()
"""
"""
import socket
client = socket.socket()
# 连接，阻塞

client.connect(('www.baidu.com',80,))

# 某种东西，检测是否已经连接成功
# 发送
client.sendall(b"GET / HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n")
client.sendall(b"GET /wupeiqi/articles/6283017.html HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n")

# 某种东西，检测是否已经返回
# 接收，阻塞
data = client.recv(8096)
headers,bodys = data.split(b'\r\n\r\n')
header_list = headers.split(b'\r\n')
for item in header_list:
    print(item)
print(bodys)
client.close()
"""
import socket
import select

class HttpRequest(object):
    def __init__(self,sk,item):
        self.sock =sk
        self.item = item
    def fileno(self):
        return self.sock.fileno()


class AsyncHttp(object):
    def __init__(self):
        self.client_list = []
        self.connections_list = []
    def start(self,item):
        try:
            sk = socket.socket()
            sk.setblocking(False)
            sk.connect((item['host'],80))
        except BlockingIOError as e:
            pass
        self.client_list.append(HttpRequest(sk,item))
        self.connections_list.append(HttpRequest(sk,item))
    def run(self):
        """
        检测 self.client_list，self.connections_list里面socket是否已经连接成功
        :return:
        """
        while True:
            # 【socket1，】
            # 【socket1，socket2,socket3】
            # 以前：select.select（【socket对象.fileno()，socket对象】）
            # 不是：select.select（【任意对象(包含fileno方法)，任意对象】）
            r,w,e = select.select(self.client_list,self.connections_list,[],0.05)
            # 可写：如果有socket和服务端连接成功：[socket2,socket3]
            # 可读：有服务端给我们返回数据【socket1，socket2】
            for conn in w:
                """连接成功"""
                host = conn.item['host']
                url = conn.item['url']
                temp = "GET %s HTTP/1.0\r\nHost: %s\r\n\r\n" %(url,host,)
                # temp = "POST %s HTTP/1.0\r\nHost: %s\r\n\r\nasdfasdfasd" %(url,host,)
                conn.sock.sendall(bytes(temp,encoding='utf-8'))
                self.connections_list.remove(conn)
            for conn in r:
                """获取响应内容"""
                func = conn.item['fn']
                data = conn.sock.recv(8096)
                func(data)
                conn.sock.close()
                self.client_list.remove(conn)
            if not self.client_list:
                break


def done(content):
    print(content)


url_list = [
    {'host':'www.google.com','url':'/','fn': done},
    {'host':'www.bing.com','url': '/','fn': done},
    {'host':'www.cnblogs.com','url': '/wupeiqi/articles/6283017.html','fn': done}
]
ioloop = AsyncHttp()
for item in url_list:
    ioloop.start(item)
    print(item)

ioloop.run()



