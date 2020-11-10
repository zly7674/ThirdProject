from socket import *

#创建套接字
sockfd=socket()
#发起连接
server_addr=('127.0.0.1',8888)
sockfd.connect(server_addr)
#消息收发
sockfd.send(input().encode())
data=sockfd.recv(1024)
print('From server:',data.decode())
#关闭
sockfd.close()
c=input()