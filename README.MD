# Collection of tools for manipulating MP3 Libraries
## Whats needed?
Python3 and Pip in path.
Run install-dependencies.bat to install required dependencies.
  

## List of tools

### 1.) resize_id3_thumbs.py:

Scans for album covers that are over MAX_SIZE (default 500x500) and resizes them to max size respecting the aspect ratio.

**Usage:**
edit the file and set MAX_SIZE to any size you want.
There are 2 modes, Dry and Wet run respectvly:

	python resize_id3_thumbs.py dry
	python resize_id3_thumbs.py


### 2.) download.bat:
Downloads playlists using Youtube-dl and converts to MP3 using FFMPEG.

**Usage:** 
**NOTE:** the **"** are very important around URL
download.bat \<folder> "\<URL>"

example:

    download.bat top100beatport "https://www.youtube.com/playlist?list=PLpPqsLMfPER9WSbq3yaKXkKmtz0n5hcRe"
