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

# 在数据表中创建新的一列
cursor.execute("alter table data_info add column calib_camera_intrinsic text")
for record in records:
    # 获取calib_camera_intrinsic_path 字段的值
    calib_camera_intrinsic_path = record[5] 
    # 读取文件内容
    try:
        with open( calib_camera_intrinsic_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"File not found: { calib_camera_intrinsic_path}")
        continue  # 跳过不存在的文件
    except Exception as e:
        print(f"Error reading file: {e}")
        continue  # 跳过有错误的文件
        # 更新data_info表，        
    update_query = " update data_info  set  calib_camera_intrinsic = %s  where id = %s " # id是主键，用于标识每一行 
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
