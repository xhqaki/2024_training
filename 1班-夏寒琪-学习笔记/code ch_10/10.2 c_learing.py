from pathlib import Path
path = Path('learning_python.txt')
contents=path.read_text()
a=contents.replace('python','C')
print(a)