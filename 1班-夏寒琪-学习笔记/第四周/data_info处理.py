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
    image_timestamp BIGINT NOT NULL,  
    pointcloud_path VARCHAR(255) NOT NULL,  
    point_cloud_stamp BIGINT NOT NULL,  
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
            image_timestamp,  
            pointcloud_path,  
            point_cloud_stamp,  
            calib_camera_intrinsic_path,  
            calib_lidar_to_camera_path,  
            label_camera_std_path,  
            label_lidar_std_path  
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)  
    """
    values = (
        item['image_path'],
        int(item['image_timestamp']),  # 假设timestamp是字符串表示的整数
        item['pointcloud_path'],
        int(item['point_cloud_stamp']),  # 同样假设是字符串表示的整数
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

cursor.execute("select * from data_info")
print(cursor.fetchone())
# 提交事务
connection.commit()

cursor.close()
connection.close()
print("All data has been inserted successfully.")
