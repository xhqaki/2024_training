import mysql.connector
from mysql.connector import Error


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
)  # 连接mysql


cursor = mydb.cursor()
cursor.execute('use itcast')  # 选用数据库itcast
cursor.execute("insert into emp values (17,'00017','alex','女','20','12345678901','shanghai','2005-1-5');")  # 插入一条新信息
print(f"Inserted {cursor.rowcount} row(s).")
cursor.execute("delete from emp where id = 16;")  # 删除id为16的用户
print(f"Delete {cursor.rowcount} row(s).")
cursor.execute("update emp set gender ='男' where id = 17;")  # 将id为17的用户性别改为男
print(f"Update {cursor.rowcount} row(s).")
cursor.execute("SELECT * from emp")  # 查询emp表中所有信息
for info in cursor.fetchall():
    print(info)  # 分行打印emp表


cursor.close()
mydb.close()
