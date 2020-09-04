from youtube_api import YouTubeDataAPI
from youtube_api import parsers
from datetime import datetime
from pathlib import Path

import youtube_dl
import os
import sys

# How to get a YT Channel ID: https://support.google.com/youtube/answer/3250431
YT_CHANNEL_ID = ""

# How to get a YT API Key:
# - https://developers.google.com/youtube/v3/getting-started
# - https://console.developers.google.com/apis/dashboard
YT_API_KEY = ""  # this key should be private!

DOWNLOAD_DIR = "videos"


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


yt = YouTubeDataAPI(YT_API_KEY)

# get all videos metadata
data = yt.get_channel_metadata(channel_id=YT_CHANNEL_ID)
playlist_id_uploads = data.get("playlist_id_uploads")
videos = yt.get_videos_from_playlist_id(playlist_id_uploads)

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

# for each public video
for idx, video in enumerate(videos):
    # prepare variables
    video_id = video.get("video_id")
    publish_date = video.get("publish_date")
    vmd = yt.get_video_metadata(video_id)
    publish_date = datetime.fromtimestamp(publish_date)
    video_title = vmd.get("video_title")
    video_description = vmd.get("video_description")
    video_url = "https://www.youtube.com/watch?v={v_id}".format(v_id=video_id)

    if publish_date.year == 2019:
        print("\nDownloading video {idx} - {title}".format(idx=idx, title=video_title))
        # download video
        force_dowload(video_url, ydl_opts)

print("Done.")
