numbers={'alex':{'1','6'},'penny':{'2','7','9'},'vincent':{'3','12','18'},'zhangsan':{'8','28'},'lisi':{'5','68','88'}}
for name,number in numbers.items():
    print(f'{name}喜欢的数字是:')
    for num in number:
        print(num)