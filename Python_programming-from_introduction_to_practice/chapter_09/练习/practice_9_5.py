class User:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nthe name of user is {self.first_name} {self.last_name}.")
        
    def greet_user(self):
        print(f"hello, {self.first_name}.")      

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_0 = User(f_name = 'aa', l_name = 'bb')
user_0.describe_user()
user_0.greet_user()
for value in range(0, 3):
    user_0.increment_login_attempts()
print(f"\n{user_0.login_attempts}")
user_0.reset_login_attempts()
print(f"\n{user_0.login_attempts}")