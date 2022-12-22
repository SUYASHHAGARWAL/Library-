import pymysql as SQL
try:
    conn=SQL.connect(host='localhost',port=3306,user='root',passwd='1234',database='library')
    smt=conn.cursor()
    q='create table libraria(libid int primary key,name varchar(25))'
    smt.execute(q)
    conn.commit()
    print("Table Created Successfully")
    conn.close()
except Exception as err:
    print("Error:",err) 
