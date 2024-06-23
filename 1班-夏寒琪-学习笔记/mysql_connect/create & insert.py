import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('mysql://root:123456@localhost/itcast', echo=True)

meta_data = sqlalchemy.MetaData()

person = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
)
meta_data.create_all(engine)

# 增加单条数据
person_insert = person.insert()
insert_one = person_insert.values(name='alex',birthday='2000-1-1')
with engine.connect() as conn:
    conn.execute(insert_one)
    conn.commit()

# 增加多条数据
insert_multiple = person.insert()
with engine.connect() as conn:
    conn.execute(insert_multiple, [
        {"name": "bob", "birthday": "2001-06-29"},
        {"name": "charlie", "birthday": "2002-08-18"},
    ])
    conn.commit()