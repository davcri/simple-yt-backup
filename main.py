from datetime import datetime
from pathlib import Path
from youtube_dl import DateRange

import youtube_dl
import os
import sys

# Change this link to the channel that you want to backup
YT_CHANNEL = "https://www.youtube.com/channel/UCFVgUrvckqp0i_pbCj3wjfA"
YEAR = None  # set None if you want to download everything. Set the year (YYYY, eg: `2019` integer) if you want to download only videos from a specific year.
DOWNLOAD_DIR = "videos-{}".format(YEAR) if YEAR != None else "videos"


def daterange_for_year(year: int):
    start = "{}0101".format(year)
    end = "{}1231".format(year)
    return DateRange(start=start, end=end)


def force_dowload(video_url, opts):
    """Workaround to force retry a video download.
    Sometimes youtube_dl stops downloading a video because of:
    `ERROR: unable to download video data: <urlopen error [Errno -2] Name or service not known>`
    This function detects the error and call again itself, continuing the download process
    """
    try:
        with youtube_dl.YoutubeDL(opts) as ydl:
            ydl.download([video_url])
    except KeyboardInterrupt:
        sys.exit()
    except BaseException as e:
        print("---")
        print("Exception occurred")
        print(e)
        print("Retrying...\n")
        force_dowload(video_url, opts)


# make sure download directory exists
out_dir = Path(DOWNLOAD_DIR)
out_dir.mkdir(parents=True, exist_ok=True)
os.chdir(str(out_dir))

# youtube_dl options
ydl_opts = {
    "writethumbnail": True,
    "writedescription": True,
    "continuedl": True,
    "retries": 100,
    "fragment_retries": 100,
    "cachedir": "./_cache",
}

if YEAR != None:
    ydl_opts["daterange"] = daterange_for_year(YEAR)

force_dowload(YT_CHANNEL, ydl_opts)

print("Done.")
