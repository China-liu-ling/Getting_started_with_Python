names = ['aa', 'bb', 'cc']
print(f'Would you like to diner with me? {names[0].title()}, {names[1].title()}, {names[2].title()}')
print(f'{names[0].title()} can not arrive')
names[0] = 'dd'
print(f'Would you like to diner with me? {names[0].title()}, {names[1].title()}, {names[2].title()}')