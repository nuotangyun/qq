import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test', charset='utf8')
cur = db.cursor()
with open('qq.jpg', 'rb') as f:
    data = f.read()
try:
    sql = "insert into image values (1,%s,%s)"
    cur.execute(sql, ['qq.jpg', data])
    db.commit()
except:
    db.rollback()
cur.close()
db.cursor()
