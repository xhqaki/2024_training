messages=['hello','goodbye','good morning','good evening']
def show_messages(greeting):
    print(f'{greeting}')
for message in messages:
    show_messages(message)

#另一种
def show_messages(greeting):
    for mes in greeting:
        print(f'{mes}')
messages=['hello','goodbye','good morning','good evening']
show_messages(messages)