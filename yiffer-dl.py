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
    # If yiffer starts appending slashes, this breaks.
    image_url = comic_url + "/" + image_src

    # Download path should be ./dl/xx.jpg
    dl_path = os.path.join(
        dl_dir,
        "{0:02d}.jpg".format(image_id)
    )

    # Actually get the image data
    image_data = requests.get(image_url)

    if image_data.status_code != 200:
        print("Image {}: Status code: {}"
              .format(image_id, image_data.status_code))
        return image_data.status_code

    with open(dl_path, "wb") as f:
        f.write(image_data.content)


if __name__ == "__main__":
    os.mkdir(DOWNLOAD_LOCATION)
    download_comic(URL, DOWNLOAD_LOCATION)
