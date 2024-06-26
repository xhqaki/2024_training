# 5.31
VS CODE已安装并下载Python扩展包。
# 6.3 
## ch_2
### 变量
变量名只能包含数字、字母和下划线_，且数字不能打头。变量名不能包含空格。  
变量名是分大小写的，name和Name是两个不同的变量。  
如果变量里有引号，如我们要打印let's go这句话，为了避免出现错误，应该将代码写作`print('let\'s go')`,当反斜杠放在单引号或双引号前时会被看作一个整体。  
### 字符串
字符串需要被单引号或双引号框起来。  
title()是将字符串的首字母变成大写，upper()是把所有字母变成大写，lower()是将所有字母变成小写。  
如果要在打印时引用已经定义过的字符串，需要在引号前加上f,否则不会取值  
rstrip(),lstrip(),strip()分别是删除右边空白，删除左边空白和删除所有空白  
### 数
可以对数进行加减乘除运算，数的类型可以通过命令改变。  
## ch_3
### 列表
用[]表示列表，各元素中间用","隔开。  
获取元素时，可以使用命令list[i],则会返回第i+1个元素名字，即索引从0开始。  
修改元素可以直接对该元素进行赋值处理。  
len(list) #list的元素个数
#### 添加元素
list.append() #在列表末尾添加元素
list.insert() #添加元素，可以用索引指定位置
#### 删除元素
del list[i] #删除第i+1个元素  
list.pop(i) #不加索引时删除最末一个元素，加索引时删除指定位置的元素  
#### 排序
list.sort() #永久正向排序  
list.sort(reverse=True) #永久反向排序  
list.reverse() #永久反向排序  
sorted(list) #暂时正向排序  
sorted(list,reverse=True) #暂时反向排序
# 6.4
## ch_4
### 循环
基本语法：  
```python
for 名字 in 列表：  
     print()  
```
在循环中需要注意缩进的问题。  
### range()
range(1，5)返回1到4，可给range()添加步长，比如range(1，6，2)会返回1，3，5。  
### 列表推导式
列表推导式将for循环和创建新元素的代码合成到一行，并自动追加新元素。  
例：cube = [num**3 for num in range(1,11)]#创建1-10的三次方的列表  
### 切片
list[i:n]表示取list中第i+1位到第n+1位  
### 列表复制
要复制列表，可以创建包含整个列表的切片，方法是省略起始索引和终止索引，比如要复制list，可以用命令行list1=list[:],不能直接写list1=list，如果这样写了list1和list和同时变化，即list1和list是关联上的。  
### 元组
元组由圆括号来标识，元素不可修改，但能重新进行整体赋值  
## ch_5
### if语句
```python
if 条件：  
      执行语句  
elif 条件：  
      执行语句  
else ：  
      执行语句  
```
### 检查列表非空
```python
if list：
    执行语句
else
    print("这是一个空列表")
```
# 6.5
## ch_6
### 字典
字典是一系列键值对，每个键都与一个值相关联，键和值中间用冒号连接，键值对之间用逗号分隔，字典由大括号包围。   
例：alien={'color':'green','points':5}  
修改和获取键值对的值可以直接由字典名和键名得到，比如字典名['键名']  
添加键值对可以用上述的格式直接对新键进行赋值  
删除键值对用del 字典名['键名']   
### 遍历字典
以下由字典名为alien为例：  
遍历所有字符对：  
for key,value in alien.items():  
遍历所有键：  
for key in alien.keys():
遍历所有值：  
for value in alien.values()  
如果需要按顺序返回，可以在in后面加上sorted  
## ch_7
### while循环  
基本语句：  
```python
while 条件/标志 :  
     执行语句  
```
如果break条件满足则跳出循环，如果continue条件满足则直接进行新一轮循环  
若要删除列表中一个特定的字符串，可以用这样的代码：
```python
pets=['dog','cat','bird','cat','dog','cat']
while 'cat' in pets:
     pets.remove('cat')
print(pets)
```
## ch_8
### 函数
定义函数举例：
```python
def greeting():
     print('hello')
greeting()  #调用函数
```
函数括号里可以传递参数，参数也可以自带默认值  
可以给函数设置一个返回值，随时可以调用  
#### 传递任意数量的形参：  
形参加上*即为创造一个元祖，可以接受不同数量的参数  
#### 使用任意数量的关键字实参  
形参加上两个*会创建一个字典，可以在函数中创建新的键值对  

## ch_9 
### 类
```python
 class Dog:
"""一次模拟小狗的简单尝试 """
     def __init__(self, name, age):##name和age自动传入self
     """初始化属性name和 age""" 
          self.name = name
          self.age = age
     def sit(self):
     """模拟狗狗收到命令时坐下 """
          print(f"{self.name} is now sitting.")
     def roll_over(self):
     """模拟狗狗收到命令时打滚 """ 
          print(f"{self.name} rolled over!")
##创建实例
my_dog=Dog('Willie',6) #创建狗类实例
my_dog.sit()
my_dog.roll_over() #调用类里的函数
```
### 继承
```python
class ElectricCar(Car): #已经有一个Car类，且调用了这个类
    def __init__(self, make, model, year):
     """先初始化父类属性，再初始化特有属性"""
        super().__init__(make, model, year) #继承父类属性
        self.battery_size = 40 #初始化特有属性
    def describe_battery(self):
     """打印描述电池容量的信息 """
          print(f"This car has a {self.battery_size}-kWh battery.")
#创建实例
my_leaf = ElectricCar('nissan', 'leaf', 2024) 
print(my_leaf.get_descriptive_name()) #括号里调用了父类函数
my_leaf.describe_battery()
```


