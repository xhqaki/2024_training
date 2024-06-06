def send_messages(messages,sent_message=[]):
    while messages:
        mes=messages.pop()
        print(mes)
        sent_message.append(mes)
    return sent_message
message=['hello','goodbye','good morning','good evening']
sent_message=send_messages(message[:])
print(sent_message)
print(message)