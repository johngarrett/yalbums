## about
I want these songs and albums (https://www.youtube.com/watch?v=0cmIrC9rGMU&list=PL904H6KHvziX-ZjHR1LYMucgQ_NSVlJM) avaliable offline
## scratchpad
- given youtube link, download the audio
- read the description for timestamps and song names or as the user to write it in a file
- ask for album name, artist name, album cover (maybe try to take a screenshot from video)
- split and output to dir

## scratchy scratchpad
- gettting title and description
```python
import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()

# authorize - you need to sign up for your own access key, or be rate-limited
# yt_service.developer_key = 'ABCxyz123...'
# yt_service.client_id = 'My-Client_id'

def PrintEntryDetails(entry):
    print 'Video title: %s' % entry.media.title.text
    print 'Video published on: %s ' % entry.published.text
    print 'Video description: %s' % entry.media.description.text
    print 'Video category: %s' % entry.media.category[0].text
    print 'Video tags: %s' % entry.media.keywords.text
    print 'Video watch page: %s' % entry.media.player.url
    print 'Video flash player URL: %s' % entry.GetSwfUrl()
    print 'Video duration: %s' % entry.media.duration.seconds

for entry in yt_service.GetTopRatedVideoFeed().entry:
    PrintEntryDetails(entry)
```
    - see: https://developers.google.com/youtube/1.0/developers_guide_python
- video thumbnail
    - `http://img.youtube.com/vi/<insert-youtube-video-id-here>/maxresdefault.jpg`
        - works and is high quality... might need to crop to square
        -
    - `urllib.urlretrieve("http://img.youtube.com/vi/ytvideo/0.jpg")`
- download audio
``` python
from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
```
