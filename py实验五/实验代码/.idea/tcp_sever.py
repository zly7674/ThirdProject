import socket
import json
#创建套接字
sockfd=socket.socket()
#绑定地址
sockfd.bind(('0.0.0.0',4416))
#设置监听队列
sockfd.listen(5)
#等待客户端连接
print('Waiting for connect...')
connfd,addr=sockfd.accept()
while(1):
    #收发消息
    data=connfd.recv(1024)
    if not data:
        print('欢迎下次使用，再见！！')
        break
    stu = json.loads(data)
    p = open("tcpdata.txt", "a")
    p.write(stu[0])
    p.write(" ")
    p.write(stu[1])
    p.write(" ")
    p.write(str(stu[2]))
    p.write(" ")
    p.write(str(stu[3]))
    p.write("\n")
    p.close()
    print('收到的消息：',data.decode())
    n=connfd.send('收到'.encode())
    print('发送了%d字节数据'%n)
#关闭套接字
connfd.close()
sockfd.close()