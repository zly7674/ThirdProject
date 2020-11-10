import random
def number():
    print("------------猜数字-----------")
    n=random.randint(0,500)
    while True:
        num=int(input("请输入一个整数:"))
        if num > n:
            print("你猜的数比答案大")
        elif num < n:
            print("你猜的数比答案小")
        elif num == n:
            print("你猜中了！")
            break
    strc=input("按任意键退出。。。")
passward='123456'
p=input('请输入密码:')
if p==passward:
    print('登陆成功')
    number()
else:
    print('密码错误')