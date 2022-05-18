from random import choice

lottery = [
    'a', 'b', 'c', 'd', 'e',
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
]
answer = []
for x in range(0, 4):
    answer.append(choice(lottery))

print("If your lottery contains the following four numbers, "
"you will win the grand prize: ")
print(f"\t{answer}")