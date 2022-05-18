pizzas = ['aa', 'bb', 'cc', 'dd', 'ee']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza.')
print('I really like pizza.')

print('\nThe first three items in the list are:')
print(pizzas[:3])
print('Three items from the middle of the list are:')
print(pizzas[1:4])
print('The last three items in the list are:')
print(pizzas[-3:])