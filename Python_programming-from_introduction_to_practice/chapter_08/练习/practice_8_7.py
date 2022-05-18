def make_album(name_singer, name_album, number_song = None):
    if number_song:
        message = {'singer': name_singer, 'album': name_album, 'number': number_song}
    else:
        message = {'singer': name_singer, 'album': name_album}
    return message

#主程序
for number in range(0,3):
    name_of_singer = input("enter the name of singer: ")
    name_of_album = input("enter the name of album: ")
    number_of_song = input('enter the number of song in album: ')
    full_name = make_album(name_album=name_of_album, name_singer=name_of_singer, number_song=number_of_song)
    print(full_name)