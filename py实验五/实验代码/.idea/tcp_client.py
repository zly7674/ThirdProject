from socket import *
import json
#创建套接字
sockfd=socket()
#发起连接
server_addr=('127.0.0.1',4416)
sockfd.connect(server_addr)
while(1):
    #收发消息
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
    sockfd.send(string.encode())
    data=sockfd.recv(1024)
    print('来自服务器端：',data.decode())
    flag=input(('是否继续输入学生信息?（Y/N）\n'))
    if flag=='N':
        print('欢迎下次使用，再见！！')
        break
#关闭套接字
sockfd.close()

# json.loads  ： 将python字符串 转换为 python字典/列表
# json.dumps  :  将python字典/列表 转换为 python字符串

