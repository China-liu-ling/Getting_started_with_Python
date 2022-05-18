shuyu = {
    'aa': 'bb', 
    'cc': 'dd',
    'dd': 'ee',
    'ff': 'gg',
    'hh': 'ii',
}
renyuan = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg']

for name in shuyu.keys():
    print(f'Hi, {name.title()}.')
    if name in renyuan:
        print(f' Thank you for the survey.')
    else:
        print(f' Would you like to participate in?')