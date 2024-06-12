
from sqlalchemy import create_engine,text
engine = create_engine('mysql://root:123456@localhost/itcast', echo=True)
conn = engine.connect()

query = text('select * from emp')
result = conn.execute(query)  # 查看原始数据集
for line in result:
    print(line)
query1 = text("insert into emp values (17,'00017','alex','女','20','12345678901','shanghai','2005-1-5')")  #增
result1 = conn.execute(query1)
query3 = text("delete from emp where name = 'alex' ")  # 删
result3 = conn.execute(query3)
query4 = text("update emp set name = 'penny' where id = 15")  # 改
result4 = conn.execute(query4)
query2 = text('select * from emp')  # 查
result2 = conn.execute(query2)

for line in result2:
    print(line)

conn.close()
