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

# 查询表中所有记录
query = person.select()
results = conn.execute(query)

for row in results:
    print(row)

# 查询ID为1的信息
query2 = person.select().where(person.c.id == 1)
result = conn.execute(query2)
print(result.fetchall())

# 查询ID小于4大于1的信息
query3 = person.select().where(person.c.id > 1).where(person.c.id < 4)
result1 = conn.execute(query3)
print(result1.fetchall())

# 查询ID=1或生日在2000-1-1之后和2002-8-18之前的信息
query4 = person.select().where(
    or_(
        person.c.id == 1,
        and_(
            person.c.birthday > "2000-1-1",
            person.c.birthday < "2002-8-18"
        )
    )
)
result2 = conn.execute(query4)
print(result2.fetchall())

