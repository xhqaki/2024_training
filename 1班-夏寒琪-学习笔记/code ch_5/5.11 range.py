numbers=[]
for num in range(1,10):
    numbers.append(num)
print(numbers)
for num in numbers:
    if num==1:
        print(f'{num}st')
    elif num==2:
        print(f'{num}nd')
    elif num==3:
        print(f'{num}rd')
    else:
        print(f'{num}th')
