rivers = {
    'chang jiang': 'China',
    'mississippi': 'America',
    'nile': 'egypt'
}

for river, nation in rivers.items():
    print(f'The {river.title()} runs through {nation.title()}.')
print('\n')
for river in rivers.keys():
    print(f'{river.title()}')
print('\n')
for nation in rivers.values():
    print(f'{nation.title()}')