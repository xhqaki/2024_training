from random import choice
mix=[18,8,28,58,68,88,66,6,16,86,'x','w','h','a','o']
lottery=[]
while len(lottery)<4:
    a=choice(mix)
    if a not in lottery: #避免彩票号有重复的数字或字母
      lottery.append(a)
print('彩票号是')
print(lottery)
print(f'如果你的彩票号是：')
for b in lottery:
   print(b,end=',')
print('恭喜你中奖了！')