import pymysql
conn = pymysql.Connect(host='localhost',user='root',passwd='123456',db='1440501226')
cur = conn.cursor()
sql=  "call stu_age(001,@sage) ;"
cur.execute(sql)
for i in cur:
    print( i)
conn.commit()
cur.close()
conn.close()
