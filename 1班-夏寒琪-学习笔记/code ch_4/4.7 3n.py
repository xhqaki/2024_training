#3的倍数，创建一个列表，其中包含3-30内能被3整除的数，再使用一个for循环将这个列表中的数打印出来
number=[]
for num in range(3,31,3):
    number.append(num)
for num in number:
    print(num)