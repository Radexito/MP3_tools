from __future__ import unicode_literals
import youtube_dl
import os, sys
import subprocess
import argparse

parser = argparse.ArgumentParser(prog='download.py', usage='%(prog)s <FOLDER> <URL>')
parser.add_argument("folder")
parser.add_argument("URL")
args = parser.parse_args()

def download(folder,url):
    os.mkdir(folder)
    os.system('youtube-dl -f bestaudio[ext=m4a] --embed-thumbnail --add-metadata --extract-audio --audio-format mp3 --audio-quality 320k  -i "'+url+'" -o '+folder+"/%(title)s.%(ext)s")

if(os.path.isdir(args.folder)):
    print(args.folder + " Already exists")
    if input("are you sure? (y/n)") != "y":
        exit()
    
print("Folder: ", args.folder)
print("URL: ", args.URL)
download(args.folder,args.URL)
