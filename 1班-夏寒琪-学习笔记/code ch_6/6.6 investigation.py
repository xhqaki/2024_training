people=['jen','sarah']
favorite_languages={'jen':'python','sarah':'c','edward':'rust','phil':'python'}
for name in  favorite_languages.keys():
    if name in people:
        print(f'{name}, thank you for accepting our investigation')
    else:
        print(f'hello,{name}.can you take part in our investigation?')