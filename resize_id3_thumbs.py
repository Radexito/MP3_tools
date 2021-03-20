import os, sys
from io import BytesIO
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.id3 import APIC
from PIL import Image
import numpy

max_size = 500, 500
directory = "songs"
dryrun = False


if(len(sys.argv) > 1):
    print(sys.argv[1])
    if(sys.argv[1] == "dry"):
        dryrun = True
        print("DRY RUN ENABLED - NO FILES WILL BE MODIFIED.")


for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        song_path = os.path.join(directory, filename)
        tags = ID3(song_path)

        thumb = tags.getall("APIC")
        if(len(thumb)):
            img = Image.open(BytesIO(thumb[0].data))

            if(img.size > max_size):
                print(song_path + " is: ", img.size)
                if(dryrun == False):
                    print("Creating thumb")
                    img.thumbnail(max_size)
                    np_arr = numpy.array(img)

                    tags.delall("APIC")

                    img_byte_arr = BytesIO()
                    img.save(img_byte_arr, format='JPEG')
                    img_byte_arr = img_byte_arr.getvalue()
                    tags.add(APIC(
                        encoding=3,
                        mime='image/jpeg',
                        type=3, desc=u'Cover',
                        data=img_byte_arr
                    ))

                    print("Saving file")
                    tags.save(v2_version=3)

                    thumb = tags.getall("APIC")[0]
                    img = Image.open(BytesIO(thumb.data))
                    print("Output Pic size: ", img.size)
            else:
                print("Skipping - " + song_path)
        else:
            print("No Coverart")

        print("---------------------------------------")
    else:
        print("No files in dir")
exit()

