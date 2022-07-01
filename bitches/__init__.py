# how about you import some bitches
import requests
from os import mkdir, sep
from random import randint
from threading import Thread

sfw_api = 'https://api.waifu.pics/sfw/waifu'
nsfw_api = 'https://api.waifu.pics/nsfw/waifu'


def get(directory="bitches", amount=randint(5, 10), nsfw=False):
    """can choose directory name too"""
    try:
        mkdir(directory)
    except Exception as e:
        print(e)
        pass
    for i in range(amount):
        Thread(target=bitches, args=(directory, amount, nsfw)).start()


def bitches(dir_, amount=randint(3, 7), nsfw=False):
    for i in range(amount):
        if nsfw:
            req_url = requests.get(nsfw_api)
        else:
            req_url = requests.get(sfw_api)
        url = req_url.json()['url']
        if not req_url.ok:
            print("error: " + str(req_url))
        with open(dir_ + sep + url[21:], 'wb') as f:
            response = requests.get(url, stream=True)
            for block in response.iter_content(1024):
                if not block:
                    break
                f.write(block)

