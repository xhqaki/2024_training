pet1={'name':'mao','owner':'alex','class':'cat'}
pet2={'name':'gou','owner':'penny','class':'dog'}
pet3={'name':'niao','owner':'vincnet','class':'bird'}
pets={'pet1':{'name':'mao','owner':'alex','class':'cat'},
      'pet2':{'name':'gou','owner':'penny','class':'dog'},
      'pet3':{'name':'niao','owner':'vincnet','class':'bird'}}
for pet,information in pets.items():
    print(f'{pet}名字是'+information['name']+
          '类型是'+information['class']+
          '主人是'+information['owner']
          )