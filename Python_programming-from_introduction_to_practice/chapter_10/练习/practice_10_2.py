with open('learning_python.txt') as file_object:
    contexts = file_object.read()
    contexts = contexts.replace('python', 'C')
    print(contexts.rstrip())