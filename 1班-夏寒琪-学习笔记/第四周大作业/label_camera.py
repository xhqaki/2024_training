import mysql.connector
from mysql.connector import Error
import json
import os


# 连接我的mysql数据库
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="test"
)

cursor = connection.cursor()

# 查询data_info表中的所有记录
query = "SELECT * FROM data_info"
cursor.execute(query)
records = cursor.fetchall()
print(records)

cursor.execute("alter table data_info add column label_camera text")
for record in records:

    # 获取label_camera_std_path字段的值（它是record的第6个元素）
    label_camera_std_path = record[5]

    # 读取文件内容）
    try:
        with open(label_camera_std_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"File not found: { label_camera_std_path}")
        continue  # 跳过不存在的文件
    except Exception as e:
        print(f"Error reading file: {e}")
        continue  # 跳过有错误的文件

    update_query = " UPDATE data_info  SET  label_camera_std = %s  WHERE id = %s  -- 假设id是主键，用于标识每一行  "
    try:
        cursor.execute(update_query, (file_content, record[0]))  # id是record的第1个元素
    except Error as e:
        print(f"Error updating data in MySQL: {e}")
        connection.rollback()  # 如果有错误，回滚事务

    # 提交事务
connection.commit()

cursor.close()
connection.close()
print("All file contents have been stored successfully.")