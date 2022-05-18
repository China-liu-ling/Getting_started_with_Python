cities = {
    'Xi An': {
        'county': 'China',
        'population': 1200_0000,
        'fact': 'quanyunhui'
    },
    'Tokyo': {
        'county': 'Jepan',
        'population': 1350_0000,
        'fact': 'aoyunhui',
    },
    "New York": {
        'county': 'America',
        'population': 853_7673,
        'fact': 'crime',
    },
}

for city, city_info in cities.items():
    print(f"\n{city}")
    for key, value in city_info.items():
        print(f"\t{key}: {value}")

    #print(f"\tcounty: {city_info['county']}")
    #print(f"\tpopulation: {city_info['population']}")
    #print(f"\tfact: {city_info['fact']}")