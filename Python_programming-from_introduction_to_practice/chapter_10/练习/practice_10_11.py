import json

number = input("Please enter your favorite number: ")

file_name = 'favorite_number.json'

with open(file_name, 'w') as f_0:
    json.dump(number, f_0)

with open(file_name, 'r') as f_1:
    number = json.load(f_1)

print(f"I know your favorite number! It's {number}.")