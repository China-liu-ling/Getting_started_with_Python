try:
    with open('cats.txt', 'r') as f_0:
        cats = f_0.read()
    with open('dogs.txt', 'r') as f_1:
        dogs = f_1.read()
except FileNotFoundError:
    print("file does not exist")
else:
    print(f"{cats.rstrip()}")
    print(f"\n{dogs.rstrip()}")