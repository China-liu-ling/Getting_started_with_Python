#问卷的答案
answer = {}

#控制循环的标记
active = True

#用户填写调查问卷
while active:
    names = input("What's your name? (enter quit to quit) ")
    if names == 'quit':
        break
    message = 'If you could visit one place in the world, where would you go? '
    places = input(message)
    answer[names] = places

#打印调查问卷
print('\n')
for name, place in answer.items():
    print(f'{name}: {place}.')