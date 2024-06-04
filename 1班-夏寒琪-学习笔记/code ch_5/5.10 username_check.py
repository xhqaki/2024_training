current_users=['Admin','Zhangsan','lisi','wangwu','zhaoliu']
current_users1=[] #创建current_users的小写副本
for name in current_users:
    current_users1.append(name.lower())
new_users=['alex','penny','admin','zhangsan','vincent']
for newuser in new_users:
    if newuser.lower() in current_users1:
        print(f'用户名{newuser}已被使用，请输入别的用户名')
    else:
        print(f"用户名{newuser}未被使用")