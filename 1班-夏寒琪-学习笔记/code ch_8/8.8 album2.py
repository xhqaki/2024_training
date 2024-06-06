def make_album(artist,title,num = ''):
    artist_album = {'artist' : artist,'album' : title}
    if num:
        artist_album['number'] = num
    return artist_album
#while artist!='quit' and title!='quit':
 #   artist=input('请输入歌手的名字：')
  #  title=input('请输入专辑的名字：')
   # album=make_album(artist,title)
    #print(album)

print("Enter 'quit' at any time to stop.")
while True:
    title = input("What's your favorite album? ")
    if title == 'quit':
        break
    artist = input("Who's the artist? ")
    if artist == 'quit':
        break
    
    album = make_album(artist,title)
    print(album)