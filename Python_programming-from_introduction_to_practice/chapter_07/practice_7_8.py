sandwich_orders = ['aa', 'bb', 'cc', 'dd', 'ee'] 
finished_sandwiches = []

#三明治名单里的三明治移到已做好的名单里
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

#打印已做好的三明治名单
print('\nThese are a prepared sandwiches.')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich}')