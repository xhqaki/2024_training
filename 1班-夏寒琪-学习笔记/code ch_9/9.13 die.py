from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        a=0
        while a!=10:
            print(f'第{a+1}次投掷结果是：')
            print(randint(1,self.sides))
            a+=1
die1=Die()
die1.roll_die()
die2=Die(10)
die2.roll_die()
die3=Die(20)
die3.roll_die()
