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

cursor.execute("alter table data_info add column calib_camera_intrinsic text")
for record in records:
    # 假设record是一个元组，其中包含id和其他字段
    # 你可以通过索引或列名来访问它们（如果cursor是DictionaryCursor）

    # 示例：获取image_path字段的值（这里假设它是record的第一个元素）
    calib_camera_intrinsic_path = record[5]  # 或者使用record['image_path']，如果cursor是DictionaryCursor

    # 读取文件内容（这里假设是文本文件）
    try:
        with open( calib_camera_intrinsic_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"File not found: { calib_camera_intrinsic_path}")
        continue  # 跳过不存在的文件
    except Exception as e:
        print(f"Error reading file: {e}")
        continue  # 跳过有错误的文件

        # 更新data_info表，添加或更新file_content列
        # 注意：这里假设你有一个名为file_content的列来存储内容

    update_query = " UPDATE data_info  SET  calib_camera_intrinsic = %s  WHERE id = %s  -- 假设id是主键，用于标识每一行  "
    try:
        cursor.execute(update_query, (file_content, record[0]))  # 假设id是record的第二个元素
    except Error as e:
        print(f"Error updating data in MySQL: {e}")
        connection.rollback()  # 如果有错误，回滚事务

    # 提交事务
connection.commit()

cursor.close()
connection.close()
print("All file contents have been stored successfully.")
