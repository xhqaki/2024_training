class restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f'该餐馆名字叫{self.restaurant_name},是一家{self.cuisine_type}')
    def open_restaurant(self):
        print('该餐馆正在营业')
restaurant1=restaurant('美味餐厅','火锅店')
restaurant.describe_restaurant(restaurant1)
restaurant2=restaurant('不是特别美味餐厅','不辣的饭店')
restaurant.describe_restaurant(restaurant2)
restaurant3=restaurant('无敌美味餐厅','烤肉店')
restaurant.describe_restaurant(restaurant3)
