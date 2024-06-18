import json
import os
import mysql.connector
from mysql.connector import Error

# 连接我的mysql数据库
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="test"
)

cursor = connection.cursor()
# 创建一个名为data_info的新表用来储存data_info里的信息
query1 = """
CREATE TABLE data_info (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    image_path VARCHAR(255) NOT NULL,  
    pointcloud_path VARCHAR(255) NOT NULL,  
    calib_camera_intrinsic_path VARCHAR(255) NOT NULL,  
    calib_lidar_to_camera_path VARCHAR(255) NOT NULL,  
    label_camera_std_path VARCHAR(255) NOT NULL,  
    label_lidar_std_path VARCHAR(255) NOT NULL  
);
"""
cursor.execute(query1)
# 加载JSON数据
with open('data_info.json', 'r') as file:
    data_info = json.load(file)

# 通过遍历循环将data_info里的信息储存到新建的表中
for item in data_info:
    query = """  
        INSERT INTO data_info (  
            image_path,  
            pointcloud_path,  
            calib_camera_intrinsic_path,  
            calib_lidar_to_camera_path,  
            label_camera_std_path,  
            label_lidar_std_path  
        ) VALUES (%s, %s, %s, %s, %s, %s)  
    """
    values = (
        item['image_path'],
        item['pointcloud_path'],
        item['calib_camera_intrinsic_path'],
        item['calib_lidar_to_camera_path'],
        item['label_camera_std_path'],
        item['label_lidar_std_path']
        )

    try:
        cursor.execute(query, values)
    except Error as e:
        print(f"Error inserting data into MySQL: {e}")
        connection.rollback()  # 如果有错误，回滚事务


# 提交事务
connection.commit()

cursor.close()
connection.close()
print("All data has been inserted successfully.")
