with open('learning_python.txt') as file_object:
    context = file_object.read()
    print(context.rstrip())
print("\n")

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
print("\n")

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())