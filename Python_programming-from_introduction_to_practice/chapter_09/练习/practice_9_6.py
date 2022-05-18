class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(f"The name of restaurant is {self.restaurant_name}.")
        print(f"The type of restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is in business.")


class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['aa', 'bb', 'cc']

    def describe_flavors(self):
        print(f"{self.flavors}")


my_restaurant = IceCreamStand(name='ee', type='ff')
my_restaurant.describe_flavors()