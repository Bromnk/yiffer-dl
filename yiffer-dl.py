#!/usr/bin/env python3
"""
Download all pages of a yiffer.xyz comic into a directory (./dl by default).

Takes yiffer url as an argument

No license
"""

from sys import argv
import requests
import os

# Constants
MIN_DELAY = 2  # seconds
DOWNLOAD_LOCATION = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "dl/")
USER_AGENT = "Yiffer-dl V0 <notandinotandi@gmail.com> (bot)"

if len(argv) != 2:
    print("I want one and only one full yiffer.xyz url!")
    exit(1)

URL = argv[1]


def download_comic(
    url,
    dl_dir,
    min_delay=MIN_DELAY,
    user_agent=USER_AGENT
):
    image_id = 1
    err = None
    while err is None:
        # form: ../comics/<name>/xx.jpg
        image_src = os.path.join(
            "../comics/", url.split("/")[-1], "{0:02d}.jpg".format(image_id))
        print("Downloading image {}".format(image_id))
        err = _download_image(url, dl_dir, image_id, image_src)
        image_id = image_id + 1

    print("Done! Happy yiffing~")


def _download_image(comic_url, dl_dir, image_id, image_src):
    # make url
    # TODO: If yiffer starts appending slashes, this breaks.
    image_url = comic_url + "/" + image_src
    # Open file and download image
    with open(os.path.join(dl_dir, "{0:02d}.jpg".format(image_id)), "wb") as f:
        # GET request to image path
        image_data = requests.get(image_url)

        # Handle http error
        if image_data.status_code != 200:
            print("Image {}: Status code: {}".format(
                image_id, image_data.status_code))
            return 1

        # Write to file
        f.write(image_data.content)


if __name__ == "__main__":
    os.mkdir(DOWNLOAD_LOCATION)
    download_comic(URL, DOWNLOAD_LOCATION)
