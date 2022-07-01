# how about you import some bitches
import requests
from os import mkdir, sep
from random import randint
from threading import Thread

base = 'https://api.waifu.pics/nsfw/'
endpoints = [
    'waifu',
    'neko',
    'trap',
    'blowjob'
]

def get(directory: str = "bitches", amount: int = randint(5, 10), endpoint: str = 'waifu'):
    '''can choose directory name too'''
    try:
        mkdir(directory)
    except Exception:
        pass
    
    if endpoint not in endpoints:
        raise Exception(f'Endpoint does not exist!\nValid endpoints: {", ".join(endpoints)}')
    
    for i in range(amount):
        Thread(target=bitches, args=(directory, amount, endpoint)).start()

def bitches(dir_: str, amount: int = randint(5, 10), endpoint: str = 'waifu'):
    req_url = requests.get(base + endpoint)
    url = req_url.json()['url']
    if not req_url.ok:
        print("error: "+req_url)
    with open(dir_+sep+url[21:], 'wb') as f:
        response = requests.get(url, stream=True)
        for block in response.iter_content(1024):
            if not block:
                break
            f.write(block)