from socket import *
from bll import *
import json
import re
import random
import time
#创建套接字
sockfd=socket()
#绑定地址
sockfd.bind(('192.168.1.3',a))
#设置监听队列
sockfd.listen(5)



#等待客户端连接
print('Waiting for connect...')
connfd,addr=sockfd.accept()
print('Connect from:(\'192.168.1.107\',%d)'%a)
while True:
    #收发消息
    records = []
    Init(records)
    flag=0
    data=connfd.recv(1024)
    if not data:
        time.sleep(20)
        data = connfd.recv(1024)
        if not data:
            print('因为你长时间未提问，您将与客服断开连接，欢迎下次再次提问，再见！！')
            break
    print(data.decode())
    pattern = r"(\S+):(\S+)"
    l = re.findall(pattern,data.decode())
    for i in records:
        if l[0][1] == i.send:
            t=i.answer
            flag=1
            break
    if flag == 1:
        print('服务器'+':'+t)
    else:
        print('(请回复:)')
        t=input('服务器:')
    n=connfd.send(t.encode())
    print('发送了%d字节数据'%n)
#关闭套接字
connfd.close()
sockfd.close()