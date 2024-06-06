class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
class Admin(User):
    def __init__(self, first_name, last_name,privilege):
        super().__init__(first_name, last_name)
        self.privilege=privilege
    def show_privileges(self):
        for pri in self.privilege:
            print(pri)
admin=Admin('Alex','Wang',['can add post','can delete post','can ban user'])
admin.show_privileges()
