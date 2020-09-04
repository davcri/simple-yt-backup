# simple-yt-backup

CLI tool that downloads public videos, thumbnails and descriptions
from YouTube channel.

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
xdg-open main.py # manually set YT_CHANNEL_ID and YT_API_KEY variables

# execute the script
python main.py
```

## Extra

Useful links:

- https://github.com/ytdl-org/youtube-dl/
- Python Youtube API doc: https://youtube-data-api.readthedocs.io/en/latest/youtube_api.html
- https://www.reddit.com/r/DataHoarder/comments/672t9r/my_youtubedl_script_for_incremental_channel_backup/

## Todo

- Simplify usage by not requiring YouTube API key (but keep the code for future usage of downloading also private videos)

```sh
# date format is %Y%m%d
youtube-dl https://www.youtube.com/channel/UCFVgUrvckqp0i_pbCj3wjfA --dateafter 20180101 --datebefore 20190101
```
