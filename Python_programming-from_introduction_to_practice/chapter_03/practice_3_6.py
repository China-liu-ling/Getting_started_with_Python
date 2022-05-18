names = ['aa', 'bb', 'cc']
print(f'Would you like to diner with me? {names[0].title()}, {names[1].title()}, {names[2].title()}')
print(f'{names[0].title()} can not arrive')
names[0] = 'dd'
print(f'Would you like to diner with me? {names[0].title()}, {names[1].title()}, {names[2].title()}')
print(f'Now, we have more friends to join us. So, we must find a new bigger table.')
names.insert(0, 'ee')
names.insert(2, 'ff')
names.append('gg')
print(f'Would you like to diner with me? {names[0].title()}, {names[1].title()}, {names[2].title()}, {names[3].title()}, {names[4].title()}')