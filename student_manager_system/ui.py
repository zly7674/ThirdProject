"""
    ui 界面
    表示层
"""

from bll import *
from model import *

class StudentManagerView:
    """
        界面视图类
    """

    def __init__(self):
        # 创建逻辑控制器对象
        self.manager = StudentManagerController()

    def input_int(self, msg):
        while True:
            try:
                return int(input(msg))
            except:
                print("输入有误")

    def add_input_students(self):
        # 1. 在控制台中录入学生信息,存成学生对象StudentModel.
        stu = StudentModel()
        stu.name = input("请输入姓名:")

        stu.age = self.input_int("请输入年龄:")
        stu.score = self.input_int("请输入成绩:")

        # 2. 调用逻辑控制器的add_student方法
        self.manager.add_student(stu)
        print(self.manager)

    def output_students(self, list_target):
        """
            显示学生列表信息
        :return:
        """
        for stu in list_target:
            # print(stu)
            print("%d -- %s -- %d -- %d" % (stu.id, stu.name, stu.age, stu.score))

    def delete_student(self):
        # id = int(input("请输入需要删除的学生编号:"))
        id = self.input_int("请输入需要删除的学生编号:")
        if self.manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def modify_student(self):
        """
            修改学生信息
        :return:
        """
        stu = StudentModel()
        # stu.id = int(input("请输入需要修改的学生编号:"))
        stu.id= self.input_int("请输入需要修改的学生编号:")
        stu.name = input("请输入姓名:")
        # stu.age = int(input("请输入年龄:"))
        # stu.score = int(input("请输入成绩:"))
        stu.age = self.input_int("请输入年龄:")
        stu.score = self.input_int("请输入成绩::")

        if self.manager.update_student(stu):
            print("修改成功")
        else:
            print("更新失败")

    def output_student_by_score(self):
        """
            根据成绩显示所有学生信息
        :return:
        """
        list_target = self.manager.order_by_score()
        self.output_students(list_target)

    def display_menu(self):
        """
            显示菜单
        :return:
        """
        print('-'*20)
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩降序排列")
        print('-' * 20)

    def select_menu(self):
        """
        选择菜单
        :return:
        """
        number = input("请输入选项:")
        if number == "1":
            self.add_input_students()
        elif number == "2":
            self.output_students(self.manager.list_stu)
        elif number == "3":
            self.delete_student()
        elif number == "4":
            self.modify_student()
        elif number == "5":
            self.output_student_by_score()

    def main(self):
        """
            界面入口方法
        :return:
        """
        while True:
            self.display_menu()
            self.select_menu()