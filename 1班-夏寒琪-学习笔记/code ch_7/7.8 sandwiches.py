sandwiche_orders=['tuna sandwich','fruit sandwich','chicken sandwich','beef sandwich']
finished_sandwiches=[]
while len(sandwiche_orders)!=len(finished_sandwiches):
    for sandwich in sandwiche_orders:
        print(f'I made your {sandwich}')
        finished_sandwiches.append(sandwich)
print(finished_sandwiches)