def make_car(producer,type,**car):
    car['producer']=producer
    car['type']=type
    return car
car=make_car('suabru','outback',color='blue',tow_package=True)
print(car)