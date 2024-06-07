from pathlib import Path
path=Path('guest_book.txt')
names=''
while True:
    name =input('请输入您的名字：')
    if name =='quit':
        break
    names+=f'{name}\n'
path.write_text(names)

