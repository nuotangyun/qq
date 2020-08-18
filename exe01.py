import pymysql
import re

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='dict', charset='utf8')
cur = db.cursor()
f = open('dict.txt')
ages = []
for i in f:
    tup = re.findall(r"(\S+)\s+(.*)", i)[0]
    ages.append(tup)
f.close()
sql = "insert into words (word,mean) values (%s,%s);"

try:
    cur.executemany(sql, ages)
    db.commit()
except:
    db.rollback()
cur.close()
db.cursor()
