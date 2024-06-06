def sandwich(food):
     print(f'顾客要的三明治含有：')
     for kind in food:
          print(kind)
food=['香肠','蔬菜']
sandwich(food)
food=['香肠']
sandwich(food)
food=['香肠','沙拉酱','蔬菜']
sandwich(food)