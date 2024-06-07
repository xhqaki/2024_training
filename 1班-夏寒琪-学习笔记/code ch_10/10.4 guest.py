name=input('请输入您的名字')
from pathlib import Path
path=Path('guest.txt')
path.write_text(name)