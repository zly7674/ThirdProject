# １）添加学生信息
def add_student_info():
    L = []
    while True:
        n = input("(按回车直接退出)\n请输入名字：")
        if not n:  # 名字为空　跳出循环
            break
        try:
            a = int(input("请输入年龄："))
            s = int(input("请输入成绩："))
        except:
            print("输入无效，重新录入信息")
            continue
        info = {"name":n,"age":a,"score":s}
        L.append(info)
    print("学生信息录入完毕")
    return L

# ２）显示所有学生的信息
def show_student_info(student_info):
    if not student_info:
        print("无学生信息")
        return
    print("名字".center(8),"年龄".center(4),"成绩".center(4))
    for info in student_info:
        print(info.get("name").center(10),str(info.get("age")).center(4),str(info.get("score")).center(4))

# ３）删除学生信息
def del_student_info(student_info,del_name = ''):
    if not del_name:
        del_name = input("请输入删除的学生姓名：")
    for info in student_info:
        if del_name == info.get("name"):
            return info
    raise IndexError("没有找到%s" %del_name)

# ４）修改学生信息
def mod_student_info(student_info):
    mod_name = input("请输入修改的学生姓名：")
    for info in student_info:
        if mod_name == info.get("name"):
            a = int(input("请输入年龄："))
            s = int(input("请输入成绩："))
            info = {"name":mod_name,"age":a,"score":s}
            return info
    raise IndexError("没有找到%s" %mod_name)

# ５）按学生成绩高－低显示学生信息
def score_reduce(student_info):
    print("按学生成绩降序显示")
    mit = sorted(student_info ,key = get_score,reverse = True)
    show_student_info(mit)
# 以下二个函数用于sorted排序，　key的表达式函数
def get_age(*l):
    for x in l:
        return x.get("age")
def get_score(*l):
    for x in l:
        return x.get("score")

