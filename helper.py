import youtube_dl
import urllib.parse as urlparse
from pydub import AudioSegment
import re

class Yalbum:
    def __init__(self, url):
        self.url = url
        # self.video_key
        # self.songs

   
   
class YAPI:
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

    def split_download(songs):
        source_file = AudioSegment.from_file(save_location)
        ranges = []
        for time in songs:
            ranges.append(time)

        for i in range(len(ranges)):
            print(len(source_file))
            if i == len(ranges) - 1:
                song_file = source_file[ranges[i]:]
                print(f'From {ranges[i]} to end -- {songs[ranges[i]]}')
                song_file.export(f'./output/{songs[ranges[i]]}.mp3', format='mp3', codec='mp3')
            else:
                print(f'From {ranges[i]} to {ranges[i+1]} for song {songs[ranges[i]]}')
                song_file = source_file[ranges[i]: ranges[i+1]]
                song_file.export(f'./output/{songs[ranges[i]]}.mp3', format='mp3', codec='mp3')
    
    def get_songs():
        print("Enter/paste the timestamps. Press Ctrl+D ( or Ctrl+Z on windows ) when finished")
        print("FORMAT: ##:## Song Name")
        songs = {}
        while True:
            try:
                line = input()
            except EOFError:
                break
            time, name = line.split(' ', 1)
            mins, seconds = time.split(':')
            name.replace('/', '//')
            songs[(int(mins) * 60 + int(seconds)) * 1000] = name # mili seconds
        
        for time, name in songs.items():
            print(f'{name} @ {time}')
        return songs

    def save_song(name):
        urllib.urlretrieve("http://img.youtube.com/vi/ytvideo/0.jpg")


