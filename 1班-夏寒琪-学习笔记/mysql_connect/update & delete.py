import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import or_, and_
engine = create_engine('mysql://root:123456@localhost/itcast', echo=True)
conn = engine.connect()

meta_data = sqlalchemy.MetaData()

person = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
)

# 更新
query1 = person.update().where(person.c.id == 1).values(name="penny")
result1 = conn.execute(query1)
print(result1.rowcount)

# 检查是否更新成功
query2 = person.select().where(person.c.id == 1)
result = conn.execute(query2)
result2 = result.fetchall()
print(result2)

# 删
query3 = person.delete().where(person.c.id == 4)
result3 = conn.execute(query3)
print(result3.rowcount)