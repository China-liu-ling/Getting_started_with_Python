def send_message(print_messages):
    while print_messages:
        temp_message = print_messages.pop()
        print(f'The message have been send: {temp_message}')
        send_messages.append(temp_message)
def show_message(print_messages):
    print('\n')
    for message in print_messages:
        print(f'{message}')

messages = ['dadadad', 'fefefefe', 'uihbcajshb']
send_messages = []

send_message(messages[:])
show_message(messages)
show_message(send_messages)