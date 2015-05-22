import pickle, os, requests, shutil
from StringIO import StringIO
from PIL import Image
import warnings
warnings.filterwarnings("ignore")

photos = pickle.load(open('photos', 'r'))
print len(photos)
for i, girl in enumerate(photos):
    print i, '\r',
    try:
        os.mkdir('./data/' + str(girl))
        for photo in photos[girl]:
            try:
                data = requests.get(photo)
                i = Image.open(StringIO(data.content))
                i.save('./data/' + str(girl) + '/' + photo.split('/')[-1])
            except:
                pass
    except:
        pass
