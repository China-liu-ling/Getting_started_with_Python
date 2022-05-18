name = input("Enter your name: ")

with open('guest.txt', 'w') as f_0:
    f_0.write(name)