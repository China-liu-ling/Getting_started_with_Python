class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"As an administrator, you have the following permissions: ")
        print(f"\t{self.privileges[0]}")
        print(f"\t{self.privileges[1]}")
        print(f"\t{self.privileges[2]}")

class Admin():
    def __init__(self):
        self.privileges = Privileges()

admins = Admin()
admins.privileges.show_privileges()