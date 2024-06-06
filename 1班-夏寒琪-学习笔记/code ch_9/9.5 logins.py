class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def incremnet_login_attempts(self):
        self.login_attempts +=1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts =0
    def describe_user(self):
        print(f'该用户叫{self.last_name}{self.first_name}登录{self.login_attempts}次')
user1=User('Hanqi','Xia')
User.incremnet_login_attempts(user1)
User.reset_login_attempts(user1)
User.describe_user(user1)
