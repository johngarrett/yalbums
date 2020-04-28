## about
I want these songs and albums (https://www.youtube.com/watch?v=0cmIrC9rGMU&list=PL904H6KHvziX-ZjHR1LYMucgQ_NSVlJM) avaliable offline
## steps
- [X] given youtube link, download the audio
- [ ] read the description for timestamps and song names or as the user to write it in a file
- [ ] ask for album name, artist name, album cover (maybe try to take a screenshot from video)
- [ ] split and output to dir

## scratchy scratchpad
- updated youtube api requires oauth, oauth requires a website and shit
- video thumbnail
    - `http://img.youtube.com/vi/<insert-youtube-video-id-here>/maxresdefault.jpg`
        - works and is high quality... might need to crop to square
        -
    - `urllib.urlretrieve("http://img.youtube.com/vi/ytvideo/0.jpg")`
