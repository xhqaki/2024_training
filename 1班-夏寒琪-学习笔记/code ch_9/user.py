# User类
class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print(f'该用户叫{self.last_name}{self.first_name}')
    def greet_user(self,greeting='你好！'):
        print(f'{greeting}{self.last_name}{self.first_name}')