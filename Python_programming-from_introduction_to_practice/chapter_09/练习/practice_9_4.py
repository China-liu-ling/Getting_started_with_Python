class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 10

    def describe_restaurant(self):
        print(f"The name of restaurant is {self.restaurant_name}.")
        print(f"The type of restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is in business.")

    def set_number(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

my_restaurant = Restaurant(name='aa', type='bb')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number(number = 11)
my_restaurant.increment_number_served(number = 12)
print(f"{my_restaurant.number_served} people have eaten in my restaurant.")