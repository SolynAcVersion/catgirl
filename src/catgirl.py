#!/usr/bin/python
import requests
import sys
import argparse
import tempfile
from pathlib import Path
from io import BytesIO
from PIL import Image
from webbrowser import open as wbopen
from colorama import Fore, Style

VERSION = "0.74"

parser = argparse.ArgumentParser()
parser.add_argument(
    "-br", "--browser", action="store_true", help="open image in browser"
)
parser.add_argument(
    "-dp", "--download-path", type=Path, help="download image to specified directory"
)
parser.add_argument(
    "-r", "--rating", help="choose ratings: {safe, suggestive, borderline, explicit}"
)
parser.add_argument("-v", "--version", action="store_true", help="show version")
args = parser.parse_args()

if args.version:
    print(VERSION)
    sys.exit()


if args.rating:
    ratings = [r.strip() for r in args.rating.split(",") if r.strip()]
    rating_list = []
    for r in ratings:
        if r in ["safe", "12-", "sfw", "s"]:
            rating_list.append("safe")

        if r in ["suggestive", "16-", "S"]:
            rating_list.append("suggestive")
        if r in ["borderline", "18-", "b"]:
            rating_list.append("borderline")
        if r in ["r18", "18+", "nsfw", "explicit", "src"]:
            rating_list.append("explicit")
else:
    rating_list = ["safe", "suggestive"]


url = "https://api.nekosapi.com/v4/images/random"
params = {"limit": 1, "rating": rating_list}

try:
    res = requests.get(url, params=params)
    res.raise_for_status()
    data = res.json()
    if not data:
        print("no images found")
        sys.exit(1)
    img = data[0]
except Exception as e:
    print(f"request failed: {e}")
    sys.exit(1)

image_id = img.get("id")
image_url = img.get("url")
full_url = img.get("url")
rating = img.get("rating")
artist = img.get("artist_name")
source = img.get("source_url")

print(f"❮ Image ID: {image_id} ❯")
if rating:
    print(f"{Fore.GREEN}Rating:{Fore.RESET} {rating}")
if artist:
    print(f"{Fore.LIGHTYELLOW_EX}Artist:{Fore.RESET} {artist}")
if source:
    print(f"{Fore.LIGHTMAGENTA_EX}Source:{Fore.RESET} {source}")
print(f"URL: {image_url}")

if args.browser:
    wbopen(image_url)
else:
    try:
        img_res = requests.get(image_url)
        img_res.raise_for_status()
        pil_img = Image.open(BytesIO(img_res.content))
        pil_img.show()
    except Exception as e:
        print(f"failed to display image: {e}")

if args.download_path:
    if not args.download_path.is_dir():
        print(f"error: {args.download_path} is not a valid directory")
        sys.exit(1)
    try:
        file_res = requests.get(full_url)
        file_res.raise_for_status()
        filename = args.download_path / f"nekoget_{image_id}.png"
        with open(filename, "wb") as f:
            f.write(file_res.content)
        print(f"downloaded to {filename}")
    except Exception as e:
        print(f"download failed: {e}")
