#def show_messages(greeting):
 #   for mes in greeting:
  #      print(mes)
messages=['hello','goodbye','good morning','good evening']
#show_messages(messages)
def send_messages(greeting):
    sent_messages=[]
    for mes in greeting:
        sent_messages.append(mes)
    return sent_messages
sent_messages=send_messages(messages)
print(sent_messages)
print(messages)

