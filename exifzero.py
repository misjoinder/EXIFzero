# EXIFzero/exifzero.py

# python exifzero.py
# python exifzero.py /path/to/images/

# GPLv3 Licensed
# Python 2.x

from minimal_exif_writer import MinimalExifWriter
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
            
            img = MinimalExifWriter(fullpath)
            img.removeExif()
            img.process()
            break