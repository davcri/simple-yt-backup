# simple-yt-backup

A simple script that I created to download videos, thumbnails and descriptions
from my YouTube channel.

## Features

- Download all videos with a single command
- Automatically restart a download in case of a Python exception*
- Resume partial downloads (just run the same command again)

*Eg: in case of:

```bash
ERROR: unable to download video data: <urlopen error [Errno -2] Namer or service not known>
```

## Download and install dependencies

Make sure you have Python 3, git and
[Virtualenv](https://virtualenv.pypa.io/en/latest/)
already installed on your OS.

Then enter this commands in your terminal:

```sh
git clone https://github.com/davcri/simple-yt-backup
cd simple-yt-backup
virtuanlenv env
source env/bin/activate
pip install -r requirements.txt
```

## Run it

1. Open `simple-yt-backup.py`
2. Set the URL of a YouTube channel in the variable `YT_CHANNEL`
3. [optional] Set `YEAR` variable if you want to download only videos from a specific year
4. Save the file
5. Run it: `python main.py`

## Thanks

- [youtube_dl](https://github.com/ytdl-org/youtube-dl/)

## Extra

Useful links:

- Python Youtube API doc: https://youtube-data-api.readthedocs.io/en/latest/youtube_api.html
- https://www.reddit.com/r/DataHoarder/comments/672t9r/my_youtubedl_script_for_incremental_channel_backup/
