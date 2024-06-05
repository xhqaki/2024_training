age=int(input('你今年多少岁'))
while str(age) !='quit':
    if age<3:
        print(f'{age}岁的票价是免费')
    elif age>=3 and age<12:
        print(f'{age}岁的票价是10$')
    else:
        print(f'{age}岁的票价是15$')
    age=int(input('你今年多少岁'))
