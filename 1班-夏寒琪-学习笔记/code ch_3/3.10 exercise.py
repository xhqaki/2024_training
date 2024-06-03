color=["red","yellow","green","orange","blue"]
color.append("purple") #在末尾增加元素
print(color)
del color[1] #删除第二个元素
print(color)
color.insert(0,"white") #在首位添加元素
print(color)
color.sort() #排序（永久的）
print(color)
color.reverse() #反向排序（永久的）
print(color)
print(sorted(color)) #正向排序（暂时的）
print(color)
color.pop() #删除最末元素
print(color)
color[2]="grey" #把第三个元素改为grey
print(color)
