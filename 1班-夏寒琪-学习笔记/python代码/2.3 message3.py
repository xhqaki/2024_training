#2.3个性化消息 用变量表示一个人的名字，并向其显示一条消息。显示的消息应非常简单，下面是一个例子
#例子：Hello,Eric,would you like to learn some Python today?
name = "Eric"
print(f"Hello,{name},would you like to learn some Python today?")
#如果没有加"f"，{name}就不会被求值
#name = "Eric".upper()表示字符串字母全大写，如果是lower则是全小写，是title就是每个单词首字母大写