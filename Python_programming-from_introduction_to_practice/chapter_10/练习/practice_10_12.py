import json

def favorite_number():
    file_name = 'fnumber.json'
    try:
        with open(file_name, 'r') as f_0:
            f_number = json.load(f_0)
    except FileNotFoundError:
        f_number = input("Please enter your favorite number: ")
        with open(file_name, 'w') as f_1:
            json.dump(f_number, f_1)
    else:
        print(f"I know your favorite number! It's {f_number}.")

favorite_number()