import socket


    #创建套接字
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfd.bind(('0.0.0.0',8888))

#设置监听
sockfd.listen(5)
#等待处理客户端连接
print('等待连接......')
connfd,addr=sockfd.accept()
#收发消息
data=connfd.recv(1024)
print('接收到的消息:',data.decode())
n=connfd.send('收到'.encode())
#n=connfd.send(b'Receive your message')
print('发送了%d个字节数据'%n)
#关闭套接字
connfd.close()
sockfd.close()
c=input()





