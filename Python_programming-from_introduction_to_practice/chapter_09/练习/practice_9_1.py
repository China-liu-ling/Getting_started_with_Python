class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(f"The name of restaurant is {self.restaurant_name}.")
        print(f"The type of restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is in business.")

my_restaurant = Restaurant(name='aa', type='bb')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()