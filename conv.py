#!/bin/env python
# Requires: youtube_dl module
# Requires: ffmpeg
# Usage:
#
# python youtube2mp3.py <URL>, ...
# 
# Example:
# 
# python youtube2mp3.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

from pytube import YouTube
from moviepy.editor import *
import sys
import moviepy.editor as mp
import re
import os

tgt_folder = "./"


youtube_link = str(sys.argv[1:])
y = YouTube(youtube_link)
t = y.streams.filter(only_audio=True).all()
t[0].download()

for file in [n for n in os.listdir(tgt_folder) if re.search('mp4', n)]:
    full_path = os.path.join(tgt_folder, file)
    output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
    clip = mp.AudioFileClip(full_path) # disable if do not want any clipping
    clip.write_audiofile(output_path)   

filelist = [f for f in os.listdir("./") if f.endswith(".mp4")]
for f in filelist:
    os.remove(os.path.join("./", f))

