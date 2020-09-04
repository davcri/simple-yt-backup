# simple-yt-backup

KISS CLI tool to download public videos, thumbnails and descriptions
from YouTube channel.

## Features

- Download all videos with a single command
- Resume interrupted downloads (just run the same command again)
- Simple (~60 lines of code)
- Automatically restart a video download in case of Python exception
  - EG: in case of `ERROR: unable to download video data: <urlopen error [Errno -2] Namer or service not known>`

## Dependencies

Before using this script you need to install:

- Python 3
- Virtualenv
- pip

## Run

```sh
git clone ...
virtuanlenv env
source bin/env/activate
pip install -r requirements.txt

# open main.py
xdg-open main.py # set YT_CHANNEL variable (the URL of a YouTube channel)

# execute the script
python main.py
```

## Extra

Useful links:

- https://github.com/ytdl-org/youtube-dl/
- Python Youtube API doc: https://youtube-data-api.readthedocs.io/en/latest/youtube_api.html
- https://www.reddit.com/r/DataHoarder/comments/672t9r/my_youtubedl_script_for_incremental_channel_backup/
