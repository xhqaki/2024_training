class restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f'该餐馆名字叫{self.restaurant_name},是一家{self.cuisine_type},接待{self.number_served}人')
    def set_number_served(self,number_served):
        self.number_served=number_served
        print(f'就餐人数为{number_served}')
    def increment_number_served(self,inc_number):
        self.number_served+=inc_number
        print(f"餐厅可接待{inc_number}人")
    def open_restaurant(self):
        print('该餐馆正在营业')
my_restaurant=restaurant('美味餐厅','火锅店')

restaurant.open_restaurant(my_restaurant)
restaurant.set_number_served(my_restaurant,56)
restaurant.increment_number_served(my_restaurant,12)
restaurant.describe_restaurant(my_restaurant)


