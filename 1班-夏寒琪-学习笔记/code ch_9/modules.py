# User类
class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print(f'该用户叫{self.last_name}{self.first_name}')
    def greet_user(self,greeting='你好！'):
        print(f'{greeting}{self.last_name}{self.first_name}')

#Privileges类
class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

#Admin类
class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = Privileges()
	def show_privileges(self):
		for privilege in self.privileges.privileges:
			print(self.first_name,self.last_name,privilege)		