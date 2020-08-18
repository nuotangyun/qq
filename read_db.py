import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='stu', charset='utf8')
cur = db.cursor()
#name = input()
# sql = "select * from interest where name='%s'" % name
sql = 'select * from class1 where sex=%s and score>%s'

cur.execute(sql, ['m', 85])
# for i in cur:
#    print(i)s
# oen = cur.fetchone()
# print(oen)
# oen = cur.fetchmany(2)
oen = cur.fetchall()
print(oen)
cur.close()
db.cursor()
