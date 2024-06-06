def make_album(artist,title,num = ''):
    artist_album = {'artist' : artist,'album' : title}
    if num:
        artist_album['number'] = num
    return artist_album

album1 = make_album('GEM','paomo')
print(album1)
album2 = make_album('GEM','paomo','15')
print(album2)
album3 = make_album('jackson','dayanjing')
print(album3)
album4 = make_album('jackson','dayanjing','1')
print(album4)
album5 = make_album('joker','choubaguai')
print(album5)
album6 = make_album('joker','choubaguai','3')
print(album6)