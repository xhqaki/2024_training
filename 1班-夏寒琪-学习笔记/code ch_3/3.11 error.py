color=["red","yellow","green","orange","blue"]
#print(color[5])
#这里会报错，list index out of range，因为索引是从0开始的，color[5]实际上是第六个元素。
#解决方法是增加一个元素
color.append("grey")
print(color[5])
