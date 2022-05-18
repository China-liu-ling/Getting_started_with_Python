tip = 'how old are you (enter 0 to quit): '
years = input(tip)
years = int(years)
active = True

while active:
    if years < 3:
        print('Free movie viewing.')
    elif years <= 12:
        print('You need to pay $10.')
    else:
        print('You need to pay $15.')
    years = input(tip)
    years = int(years)
    if years == 0:
        active = False