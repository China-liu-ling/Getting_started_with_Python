def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

age = input('Enter your age: ')
home = input('Enter your hometown: ')
college= input('Enter your college: ')

user_profile = build_profile('liu', 'ling', age = age, home = home, college = college)
print(user_profile)