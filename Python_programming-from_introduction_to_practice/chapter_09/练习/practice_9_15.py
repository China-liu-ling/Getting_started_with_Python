from random import choice

"""初始化循环次数"""
number_cycles = 0

"""初始化彩票答案"""
answers = (10, 8, 'a', 'b')

"""初始化彩票的组成元素"""
lottery = [
    'a', 'b', 'c', 'd', 'e',
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
]

while True:
    """刷新判断因子"""
    active_0 = 0
    active_1 = 0

    """刷新彩票"""
    my_tickets = []

    """记录循环次数"""
    number_cycles += 1

    """生成彩票"""
    for x in range(0, 4):
        number_in_ticket = choice(lottery)                  
        my_tickets.append(number_in_ticket)

    """核对是否中奖"""
    for my_ticket in my_tickets:
        if my_ticket not in answers:
            break
        else:
            active_0 += 1

    for answer in answers:
        if answer not in my_tickets:
            break
        else:
            active_1 += 1

    """判断while循环是否结束"""
    if active_0 + active_1 != 8:
        continue
    else:
        break
     
    """显示结果"""
print("If your lottery contains the following four numbers, "
"you will win the grand prize: ")
print(f"\t{answers}")
print(f"\nYour ticket is: ")
print(f"\t{my_tickets}")
print(f"\nYour number of cycles is: ")
print(f"\t{number_cycles}")