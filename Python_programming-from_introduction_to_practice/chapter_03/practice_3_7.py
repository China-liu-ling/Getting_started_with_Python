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
print(f'Oh, my friends, our table can not send to my home on time. So, I have to invite two of you')
poped_names = names.pop()
print(f'{poped_names}, I am sorry, I must invite you next time.')
poped_names = names.pop()
print(f'{poped_names}, I am sorry, I must invite you next time.')
poped_names = names.pop()
print(f'{poped_names}, I am sorry, I must invite you next time.')
print(f'{names[0].title()}, you are still in my list')
print(f'{names[1].title()}, you are still in my list')
del names[0]
del names[1]
print(names)