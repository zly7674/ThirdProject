from socket import *
import json

#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)

#绑定地址
server_addr=('0.0.0.0',4486)
sockfd.bind(server_addr)


#收发消息
while True:
    data,addr=sockfd.recvfrom(1024)
    stu = json.loads(data)
    p = open("udpdata.txt", "a")
    p.write(stu[0])
    p.write(" ")
    p.write(stu[1])
    p.write(" ")
    p.write(str(stu[2]))
    p.write(" ")
    p.write(str(stu[3]))
    p.write("\n")
    print('保存数据成功！！')
    p.close()
    print('收到的消息：',data.decode())
    sockfd.sendto('收到'.encode(),addr)

#关闭套接字
sockfd.close()