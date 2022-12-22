import pymysql as SQL
try:
    conn=SQL.connect(host='localhost',port=3306,user='root',passwd='1234')
    smt=conn.cursor()
    q="create database library"
    smt.execute(q)
    conn.commit()
    print("Database Created Successfully")
    conn.close()
except Exception as err:
    print("Error:",err) 