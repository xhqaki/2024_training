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

# 添加pointcloud_size列到data_info表
# cursor.execute("ALTER TABLE data_info ADD COLUMN pointcloud_size BIGINT")

# 查询data_info表中的所有记录
query = "SELECT * FROM data_info"
cursor.execute(query)
records = cursor.fetchall()

# 遍历记录并更新pointcloud_size字段
for record in records:
    record_id = record[0]  # id是第一个字段
    pointcloud_path = record[2]  # pointcloud是第三个字段
    if os.path.exists(pointcloud_path):
        pointcloud_size = os.path.getsize(pointcloud_path)
        update_query = "UPDATE data_info SET pointcloud_size = %s WHERE id = %s"
        cursor.execute(update_query, (pointcloud_size, record_id))
    else:
        print(f"file not found: {pointcloud_path}")

    # 提交事务
connection.commit()

cursor.close()
connection.close()
print("All file sizes have been stored successfully.")