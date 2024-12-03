import os
import requests
import subprocess

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


# test url https://www.reddit.com/r/SFW_Rule34/top/.json?limit=1

reddit_json = requests.get(
    "https://www.reddit.com/r/background_for_a_day/.json?limit=1", headers=headers).json()
print(reddit_json["data"]["children"][0]["data"]["url_overridden_by_dest"])

subprocess.run(["./gallery-dl.bin","--filename","cum_background",reddit_json["data"]["children"][0]["data"]["url_overridden_by_dest"]])


subprocess.run(["/usr/bin/plasma-apply-wallpaperimage",f"{os.getcwd()}/gallery-dl/reddit/cum_background"])