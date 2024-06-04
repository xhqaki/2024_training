foods=("potato","tomato","vegetables","fish","meat")
for food in foods:
    print(food)
#foods[0]="cabbage",这里会报错
foods=("potato","tomato","cabbage","meat","meat")
for food in foods:
    print(food)