from bll import *
from modle import *
def meun():
    menu_info ='''－－－－－－－－－－
1）添加学生
2）显示学生
3）删除学生
4）修改学生
5）按照成绩降序排列
－－－－－－－－－－－'''
    print(menu_info)
def main():
    student_info = []
    meun()

    while True:
       
        number = input("(按回车直接退出)\n请输入选项：")
        if number == '1':
            student_info = add_student_info()
        elif number == '2':
            show_student_info(student_info)
        elif number == '3':
            try:
                student_info.remove(del_student_info(student_info))
            except Exception as e:
                print(e)            
        elif number == '4':
            try:                
                student = mod_student_info(student_info)
            except Exception as e:
                print(e)
            else:
                # 首先按照根据输入信息的名字，从列表中删除该生信息，然后重新添加该学生最新信息
                student_info.remove(del_student_info(student_info,del_name = student.get("name")))  
                student_info.append(student)
        elif number == '5':
                score_reduce(student_info)
        else:
            break

