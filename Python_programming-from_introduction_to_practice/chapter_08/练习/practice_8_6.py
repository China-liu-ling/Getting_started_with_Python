def city_county(name, nation):
    message = f"{name.title()}，{nation.title()}"
    return message

#主程序
names = input('Enter the name of city: ')
nations = input('Enter the nation of city: ')
full_name = city_county(name=names, nation=nations)
print(full_name)