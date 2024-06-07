try:
    num1=int(input('请输入第一个数：'))
    num2=int(input('请输入第二个数：'))
    result=num1+num2
    print('两数之和为:',result)
except ValueError:
    print('请输入正确的数字')