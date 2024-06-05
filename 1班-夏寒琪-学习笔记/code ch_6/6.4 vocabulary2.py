vocabulary={'print':'打印、输出','float':'浮点数','int':'整数型数据','str':'字符串','list':'列表'}
vocabulary['path']='路径'
vocabulary['step']='步长'
vocabulary['break']='跳出循环'
vocabulary['module']='模组'
vocabulary['range']='范围'
print(vocabulary)
for name,value in vocabulary.items():
    print(f'{name} 的含义是{value}')