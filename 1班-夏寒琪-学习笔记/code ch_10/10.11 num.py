#存储
from pathlib import Path
import json
number=input("请输入你喜欢的数字")
path=Path('number.json')
content=json.dumps(number)
path.write_text(content)

# 读取
path=Path('number.json')
content1=path.read_text()
number=json.loads(content1)
print(number)