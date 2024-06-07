class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f'该餐馆名字叫{self.restaurant_name},是一家{self.cuisine_type}')
    def open_restaurant(self):
        print('该餐馆正在营业')