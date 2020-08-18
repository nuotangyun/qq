import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test', charset='utf8')
cur = db.cursor()
sql = "select filename,img from image where filename='qq.jpg'"
cur.execute(sql)
data = cur.fetchone()
with open(data[0], 'wb') as f:
    f.write(data[1])

cur.close()
db.cursor()
