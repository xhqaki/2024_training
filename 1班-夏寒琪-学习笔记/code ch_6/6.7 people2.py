people={'person1':{'first_name':'Alex','last_name':'Wang','age':'22','city':'wuhan'},
        'person2':{'first_name':'Penny','last_name':'Li','age':'23','city':'beijing'},
        'person3':{'first_name':'Vincent','last_name':'Zhang','age':'24','city':'shanghai'}}
for person,information in people.items():
    print(f'{person}姓名是'+information['last_name']+information['first_name'])
    print(f'{person}年龄是'+information['age'])
    print(f'{person}居住地是'+information['city'])