favorite_numbers = {
    'aa': [1, 2, 3],
    'bb': [4, 5, 6],
    'cc': [7, 8, 9],
    'dd': [10, 11, 12],
    'ee': [13, 14, 15],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")