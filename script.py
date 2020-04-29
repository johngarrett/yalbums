import youtube_dl
import urllib.parse as urlparse
from pydub import AudioSegment

save_location = './download/temp.mp3'

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
        ydl.download([url])
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
        songs[int(time.replace(':', '')) * 100] = name # seconds
    
    for time, name in songs.items():
        print(f'{name} @ {time}')
    return songs

def split_download(songs):
    source_file = AudioSegment.from_file(save_location)
    ranges = []
    for time in songs:
        ranges.append(time)

    for i in range(len(ranges)):
        if i == len(ranges) - 1:
            song_file = source_file[ranges[i]:]
        else:
            song_file = source_file[ranges[i]: ranges[i+1]]
        song_file.export(f'./output/{songs[ranges[i]]}.mp3')

if __name__ == '__main__':
    # skip getting title and description for now
    url = input("Youtube video url: ")
    url_data = urlparse.urlparse(url)
    video_id = urlparse.parse_qs(url_data.query)["v"][0]
    print(f'video id: {video_id}')
    download_video(url)
    songs = get_songs()
    split_download(songs)
