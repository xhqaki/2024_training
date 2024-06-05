

#active
active=True
while active:
    age=input('你今年多少岁')
    if str(age)=='quit':
        active=False
    elif int(age)<3:
        print(f'{age}岁的票价是免费')
    elif int(age)>=3 and age<12:
        print(f'{age}岁的票价是10$')
    else:
        print(f'{age}岁的票价是15$')
