import os
import requests
import zipfile
from pathlib import Path

# 下载文件的URL
url = 'https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16066909684506624.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-11T14%3A46%3A34Z%2F604800%2F%2F131c2a5dcc17815aa4ff4b1f830600d15f90b9c760d97969662390530129f270'

# 下载文件保存的路径
download_path = Path('F:/1/single-vehicle-side-example_16066909684506624.zip')
download_path.parent.mkdir(parents=True, exist_ok=True)

# 下载文件
with requests.get(url, stream=True) as r:
    r.raise_for_status()  # 如果请求失败，抛出HTTPError异常
    with open(download_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# 解压文件
# 解压到F盘的同一目录下，创建一个新的文件夹来存放解压后的文件
unzip_dir = Path('F:/1/single-vehicle-side-example_16066909684506624')
unzip_dir.mkdir(parents=True, exist_ok=True)

# 使用zipfile解压文件
with zipfile.ZipFile(download_path, 'r') as zip_ref:
    zip_ref.extractall(unzip_dir)

print(f"文件已下载并解压到 {unzip_dir}")
