from socket import *
import json


HOST='127.0.0.1'
PORT=4486
ADDR=(HOST,PORT)
#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#收发消息
while True:
    stu = []
    print('接下来请输入学生信息：')
    id = input('学生id：')
    stu.append(id)
    name = input('学生姓名：')
    stu.append(name)
    age = int(input('学生年龄：'))
    while age > 50 or age < 3:
        print('输入有误，请重新输入！！')
        age = int(input('学生年龄：'))
    stu.append(age)
    score = float(input('学生成绩：'))
    while score > 100 or score < 0:
        print('输入有误，请重新输入！！')
        score = float(input('学生成绩：'))
    stu.append(score)
    string = json.dumps(stu)
    sockfd.sendto(string.encode(),ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print('From sever:',msg.decode())
    flag=input(('是否继续输入学生信息?（Y/N）\n'))
    if flag=='N':
        print('欢迎下次使用，再见！！')
        break


#关闭套接字
sockfd.close()