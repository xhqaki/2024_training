print("找到了更大的餐桌！")
invitation="可以和你吃饭吗？"
invitation_list=["alex","penny","luis"]
invitation_list.insert(0,"vincent") #添加vincent到列表首位
invitation_list.insert(2,"flower") #添加flower到列表中间
invitation_list.append("kiki") #添加kiki到列表最末
print(invitation+invitation_list[0])
print(invitation+invitation_list[1])
print(invitation+invitation_list[2])
print(invitation+invitation_list[3])
print(invitation+invitation_list[4])
print(invitation+invitation_list[5])
print(invitation_list)
print("很抱歉餐桌没到，只能邀请两位朋友吃饭")
reduction=invitation_list.pop() #被删掉的名字
print(invitation_list)
invitation_list.pop()
print(invitation_list)
invitation_list.pop()
print(invitation_list)
invitation_list.pop()
print(invitation_list)
del invitation_list[0]
print(invitation_list)
del invitation_list[0]
print(invitation_list)