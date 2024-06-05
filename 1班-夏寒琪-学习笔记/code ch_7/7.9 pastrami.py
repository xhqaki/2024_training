from itertools import count


sandwich_orders=['pastrami','tuna','fruit','pastrami','chicken','pastrami','beef']
finished_sandwiches=[]
print('烟熏牛肉卖完了')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while len(sandwich_orders)!=len(finished_sandwiches):
    for sandwich in sandwich_orders:
        print(f'I made your {sandwich}')
        finished_sandwiches.append(sandwich)
print(finished_sandwiches)