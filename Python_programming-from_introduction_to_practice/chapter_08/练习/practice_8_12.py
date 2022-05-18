def sandwich_toppings(*toppings):
    print('\n')
    print('The sandwich you ordered contains the following ingredients: ')
    for topping in toppings:
        print(f'\t-{topping}')

sandwich_toppings('aa')
sandwich_toppings('bb', 'cc')
sandwich_toppings('dd', 'ee', 'ff')