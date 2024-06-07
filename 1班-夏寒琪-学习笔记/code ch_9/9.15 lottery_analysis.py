from random import choice
mix=[18,8,28,58,68,88,66,6,16,86,'x','w','h','a','o']
lottery=[]
my_ticket=[8,28,68,88]
b=0
while my_ticket != lottery:
   lottery=[] #每次循环结束后清空lottery,避免下面的循环无法进行
   while len(lottery)<4:
    a=choice(mix)
    if a not in lottery: #避免彩票号有重复的数字或字母
      lottery.append(a)
      b+=1
print('中奖彩票号是：')
print(lottery)
print('你选择的号码是')
print(my_ticket)
print(f'一共循环了{b}次')