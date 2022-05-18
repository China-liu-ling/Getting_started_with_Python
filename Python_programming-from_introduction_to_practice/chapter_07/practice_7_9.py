sandwich_orders = ['aa', 'bb', 'cc', 'aa', 'aa'] 

#删除名单中的'aa'
print('The aa is sold out.')
while 'aa' in sandwich_orders:
    sandwich_orders.remove('aa')
print(sandwich_orders)