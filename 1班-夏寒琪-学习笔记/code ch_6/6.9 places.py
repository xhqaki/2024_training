favorite_places={'alex':{'changsha','shanghai'},
                 'penny':{'wuhan','beijing','kunming'},
                 'vincent':{'qinghai','guangzhou','hangzhou'}}
for name,places in favorite_places.items():
    print(f'{name}喜欢的地方有：')
    for place in places:
        print(place)