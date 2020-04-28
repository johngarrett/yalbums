import youtube_dl
import urllib.parse as urlparse

def download_video(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'logtostderr': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == '__main__':
    # skip getting title and description for now
    url = input("Youtube video url: ")
    url_data = urlparse.urlparse(url)
    video_id = urlparse.parse_qs(url_data.query)["v"][0]
    print(f'video id: {video_id}')
    download_video(url)
