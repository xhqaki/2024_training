#判断字符串是否相等
a="tesla"
b="Tesla"
print(a==b)
print(a==b.lower())
#判断在列表中
c=[1,2,3,4,5]
for num in c:
    if num==3:
        print("3在列表中")
#判断不在、列表中
if 6 not in c:
    print("6不在列表中")

