import youtube_dl
import urllib.parse as urlparse
from pydub import AudioSegment
import re

class Yalbum:
    def __init__(self, url):
        self.url = url
        # self.video_key
        # self.songs
        # 
        print('initalizing')
    def download_video(url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'logtostderr': True,
            'outtmpl': './download/temp.mp3', # './download/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url)
            print(info_dict.get('title'))
            ydl.download([url])
            songs = get_songs_from(info_dict.get('description'))
            split_download(songs)

    def get_songs_from(description):
    songs = {}
    parsed_description = re.findall('(\d+:\d+) (.+)', description)
    print('From the description, we found the following:')
    for time, name in parsed_description:
        mins, seconds = time.split(':')
        #TODO: handle seconds being zero
        songs[(int(mins) * 60 + int(seconds)) * 1000] = name.replace('/', '\u2215')
        print(f'{name} at {time}')
    yes = yes_or_no('Do you want to manually input the songs instead?')
    if yes:
        return get_songs
    else:
        return songs


