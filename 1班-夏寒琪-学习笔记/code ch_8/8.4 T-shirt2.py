def make_shirt(size='large',style='I love Python'):
    print(f'这件T恤尺码是:{size}，印到T恤上的字样是：{style}')
#位置形参调用
make_shirt()
make_shirt('medium',)
make_shirt('small','hello')