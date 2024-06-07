from pathlib import Path
try:
    path1=Path('cat.txt')
    path2=Path('dog.txt')
    contents1=path1.read_text()
    print(contents1)
    contents2=path2.read_text()
    print(contents2)
except FileNotFoundError:
    print('文件不存在！')