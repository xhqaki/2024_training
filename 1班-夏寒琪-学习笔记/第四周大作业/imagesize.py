import os
import mysql.connector

# 连接我的mysql数据库
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="test"
)

cursor = connection.cursor()

# 添加image_size列到data_info表
cursor.execute("ALTER TABLE data_info ADD COLUMN image_size BIGINT")

# 查询data_info表中的所有记录
query = "SELECT * FROM data_info"
cursor.execute(query)
records = cursor.fetchall()

# 遍历记录并更新image_size字段
for record in records:
    # record的第一个元素是id，第二个元素是image_path
    record_id = record[0]  # id是第一个字段
    image_path = record[1]  # image_path是第二个字段
    if os.path.exists(image_path):
        image_size = os.path.getsize(image_path)
        update_query = "update data_info set image_size = %s where id = %s"
        cursor.execute(update_query, (image_size, record_id))
    else:
        print(f"file not found: {image_path}")

    # 提交事务
connection.commit()

cursor.close()
connection.close()
print("All file sizes have been stored successfully.")