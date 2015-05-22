from api import call_api
import pickle, time
import warnings
warnings.filterwarnings("ignore")

girls = pickle.load(open('girls', 'r'))
print len(girls)
#girls=[46849]
photos={}
for i, girl in enumerate(girls):
    print str(i) + '\r',
    #albums = call_api('photos.getAlbums', owner_id=girl)
    albums=['profile']
    photos[girl]=[]
    for album in albums:
        album_photos = call_api('photos.get', owner_id=girl, album_id=album)
        #time.sleep(.1)
        if album_photos:
            for photo in album_photos:
                try:
                    photos[girl].append(photo['src_xbig'])
                except:
                    pass


print len(photos)
pickle.dump(photos, open('photos', 'w'))
