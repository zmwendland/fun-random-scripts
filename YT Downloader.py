# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 11:45:58 2022

@author: zacharywe
"""

from pytube import YouTube 

link = 'https://www.youtube.com/watch?v=0fR-oNs_Mgc'
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()`

print("Downloading...")
ys.download()
print("Download completed!!")