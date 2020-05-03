save_location = './download/temp.mp3'

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


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
def save_song(name):
    urllib.urlretrieve("http://img.youtube.com/vi/ytvideo/0.jpg")

if __name__ == '__main__':
    url = input("Youtube video url: ")
    download_video(url)
