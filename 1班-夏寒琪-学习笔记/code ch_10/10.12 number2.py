#存储
from pathlib import Path
import json
path=Path('number2.json')
def favorite_number():
    number=input("请输入你喜欢的数字")
    content=json.dumps(number)
    path.write_text(content)
try:
    from pathlib import Path
    import json
    content1=path.read_text()
    number=json.loads(content1)
    print('喜欢的数字是：',number)
except:
    favorite_number()