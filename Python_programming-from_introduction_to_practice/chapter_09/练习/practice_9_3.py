class User:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def describe_user(self):
        print(f"\nthe name of user is {self.first_name} {self.last_name}.")
        
    def greet_user(self):
        print(f"hello, {self.first_name}.")      

user_0 = User(f_name = 'aa', l_name = 'bb')
user_0.describe_user()
user_0.greet_user()

user_1 = User(f_name = 'cc', l_name = 'dd')
user_1.describe_user()
user_1.greet_user()