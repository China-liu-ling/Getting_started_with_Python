def build_profile(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car_profile = build_profile('subaru', 'outback', color = 'blue', tow_package = True)
print(car_profile)