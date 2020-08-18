import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='stu', charset='utf8')
cur = db.cursor()
try:
    name = input()
    age = int(input())
    score = float(input())
    sql = "insert into class1 (name,age,score) values (%s,%s,%s);"
    # sql = "update class1 set sex='m' where name='Dsa' "
    cur.execute(sql, [name, age, score])
    db.commit()
except Exception as e:
    db.rollback()
    print(e)

cur.close()
db.cursor()
