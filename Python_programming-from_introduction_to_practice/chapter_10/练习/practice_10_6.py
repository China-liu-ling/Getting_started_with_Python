try:
    number_0 = input("enter the first number: ")
    number_1 = input("enter the second number: ")
    print(f"{int(number_0)+int(number_1)}")
except ValueError:
    print("Make sure you enter a number.")