def make_shirt(size,style):
    print(f'这件T恤尺码是:{size}，印到T恤上的字样是：{style}')
#位置形参调用
make_shirt('小号','你好')
#关键字形参调用
make_shirt(size='小号',style='你好')