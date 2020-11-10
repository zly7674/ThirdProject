import pymysql
db = pymysql.connect( host='localhost',
                      port=3306,
                      user='root',
                      passwd='285300',
                      database='user',
                      charset='utf8'

)
cur = db.cursor()
sql = "select * from info;"
cur.execute(sql)
first = cur.fetchall()
db.commit()
cur.close()
db.close()
