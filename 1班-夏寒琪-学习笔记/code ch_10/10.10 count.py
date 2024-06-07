from pathlib import Path
path=Path('noval.txt')
content=path.read_text()
a=content.lower().count('the')
print(a)
b=content.lower().count('the ')
print(b)
