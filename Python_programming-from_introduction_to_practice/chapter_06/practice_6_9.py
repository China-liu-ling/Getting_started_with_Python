favorite_places = {
    'liu_ling': ['bayannaoer', 'xian'],
    'hu_yujiao': ['chengdu', 'haikou'],
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"\t{place}")