pizza_list=["土豆牛肉","咸蛋黄嫩鸡","黑松露牛肉"]
friend_pizzas=pizza_list[:]
pizza_list.append("腊肠")
friend_pizzas.append("榴莲")
print("My favorite pizzas are:")
for pizza in pizza_list:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)