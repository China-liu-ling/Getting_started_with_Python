current_users = ['aa', 'bb', 'cc', 'dd', 'ee']
new_users = ['gg', 'aa', 'bb', 'ff', 'zz']
for new_user in new_users:
    for current_user in current_users:
        if new_user == current_user:
            print('The name has been taken')
            break
    if new_user == current_user:
        continue
    else:
        print('The name has not been taken.')
