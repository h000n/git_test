from __future__ import unicode_literals
import youtube_dl
import string
import random
import js2py
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'download_archive': 'archive.txt',
    'ignoreerrors': True,
    'nooverwrites': True,
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',       
    'outtmpl': 'C:\\Users\\hoon\\Downloads\\video',        
    'noplaylist' : False,       
    'progress_hooks': [my_hook],
    'playlistreverse': True,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    eng = list(string.ascii_lowercase)
    ydl.download(['https://youtube.com/playlist?list=PLLM0Os9cWLB9GXc_W-DNxJJtmrW0j_qNw'])
    