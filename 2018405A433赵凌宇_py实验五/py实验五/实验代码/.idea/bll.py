from model import Records

import pymysql
from socket import *
import random
import json

a=44166

def Init(records): #初始化函数
    db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   passwd='285300',
                   database='tcp',
                   charset='utf8')
    #获取游标，创建游标对象
    cur=db.cursor()
    # 编写查询的sql
    sql = "select * from records"
    try:
        # 执行sql
        cur.execute(sql)
        # 处理结果集
        p = cur.fetchall()
        for i in p:
            record = Records()
            record.id = i[0]
            record.send = i[1]
            record.name = i[2]
            record.answer = i[3]
            records.append(record)
    except Exception as e:
        print(e)
        print("查询所有数据失败")
    cur.close()
    db.close()


def save(record):
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='285300',
                         database='tcp',
                         charset='utf8')
    # 获取游标，创建游标对象
    cur = db.cursor()
    sql = "insert into records values ('%s','%s','客服','%s');" %(record.id,record.send,record.answer)
    try:
        # 　列表中元素全是字符串，执行语句，自动识别类型
        cur.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()  # 失败回滚到操作之前的状态
        print("Faild:", e)
    # 关闭游标和数据库连接
    cur.close()
    db.close()


