# EXIFzero/checkexif.py

# python checkexif.py
# python checkexif.py /path/to/images/
# ^^ make sure to end with a /

# GPLv3 Licensed
# Python 2.x

# Requires Python Image Library!
from PIL import Image
from PIL.ExifTags import TAGS
import os, sys

photo_dir = "./"
gave_a_directory = len(sys.argv)
if(gave_a_directory > 1):
    photo_dir = sys.argv[1]

extensions = ['.jpg','.jpeg','.JPG','.JPEG']
filenames = os.listdir(photo_dir)
for filename in filenames:
    for extension in extensions:
        if((filename.rfind(extension) != -1) and (filename.rfind(extension) == (len(filename) - len(extension)))):
            # found filename with photo extension
            fullpath = os.path.join(photo_dir, filename)
            print fullpath
            img = Image.open(fullpath)
            exif = img._getexif()
            print exif
            break