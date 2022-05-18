class User:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def describe_user(self):
        print(f"\nthe name of user is {self.first_name} {self.last_name}.")
        
    def greet_user(self):
        print(f"hello, {self.first_name}.")      

class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"As an administrator, you have the following permissions: ")
        print(f"\t{self.privileges[0]}")
        print(f"\t{self.privileges[1]}")
        print(f"\t{self.privileges[2]}")

admins = Admin(f_name = 'aa', l_name = 'bb')
admins.show_privileges()