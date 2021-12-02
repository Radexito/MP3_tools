import os, sys
import  mutagen
from mutagen.easyid3 import EasyID3



max_size = 500, 500
directory = ""
dryrun = False


if(len(sys.argv) > 1):
    directory = sys.argv[1]


for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        song_path = os.path.join(directory, filename)
        try:
            tag = EasyID3(song_path)
        except:
            tag = mutagen.File(song_path, easy=True)
            tag.add_tags()
        
        if(float(max_bpm) < float(tag['bpm'][0])): 
            print("Skipping as bpm too fast", song_path)
            continue
        print(song_path)
        print('bpm: ', tag['bpm'])
        tag['bpm'] = [ str(float(tag['bpm'][0]) / 2) ]
        print('new bpm: ', tag['bpm'])
        tag.save(v2_version=3)
