pizzas = ['aa', 'bb', 'cc']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza.')
print('I really like pizza.')

friend_pizzas = pizzas[:]
pizzas.append('ee')
friend_pizzas.append('ff')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)