#how about you import some bitches
import os
import requests
from random import randint
from threading import Thread
from zipfile import ZipFile, ZIP_DEFLATED

api = 'https://api.waifu.pics/nsfw/waifu'

def get(dirr=None):
    '''can choose directory name too'''
    directory = "bitches"
    if dirr:
        directory = dirr
    try: os.mkdir(directory)
    except Exception: pass
    for i in range(randint(5, 10)):
        Thread(target=bitches, args=(directory, )).start()

def bitches(dir_):
    for i in range(randint(3, 7)):
        req_url = requests.get(api)
        url = req_url.json()['url']
        if not req_url.ok:
            print("error: "+req_url)
        with open(dir_+os.sep+url[21:], 'wb') as f:
            response = requests.get(url, stream=True)
            for block in response.iter_content(1024):
                if not block:
                    break
                f.write(block)

def tempDir():
    system = os.name
    if system == 'nt':
        return os.getenv('temp')
    elif system == 'posix':
        return '/tmp/'

def zipfile(_file):
    _zipfile = os.path.join(os.getcwd(), 'bitches.zip')
    zipped_file = ZipFile(_zipfile, "w", ZIP_DEFLATED)
    abs_src = os.path.abspath(_file)
    for dirname, _, files in os.walk(_file):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            zipped_file.write(absname, arcname)
    zipped_file.close()