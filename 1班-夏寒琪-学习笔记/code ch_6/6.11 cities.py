cities={'wuhan':{'country':'China','population':'500million','fact':'beautiful'},
        'paris':{'country':'France','population':'50million','fact':'fashion'},
        'changsha':{'country':'China','population':'400million','fact':'nice'}
        }
for city,information in cities.items():
    print(
        f'{city}位于'+information['country']+
        '人口量是'+information['population']+
        '客观事实是'+information['fact']
    )