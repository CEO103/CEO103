import json
import requests
import random
import time
from helpers.headers import headers
from threading import Thread
import secrets
from helpers.randomwords import words
import string


channels = ["901373944521691190","901374056920674334","901374077531480065","901374089539756052","901374104060428299"]


nonce = "722789522290923712"


def generate_nonce(nonce):
    return str(int(nonce) + random.randint(1, 100))

def sendM(message:str, channel=False):
    f = open("helpers/data.json")
    data = json.load(f)
    data["content"] = message
    data["nonce"] = generate_nonce(nonce)
    data = json.dumps(data)
    try:
        r = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(random.choice(channels) if not channel else channel), headers=random.choice(headers), data=data)
    except Exception:
        print("Exception")

def sendMessage():
    n = 0
    while True:
        mLen = random.randint(1,30)
        message = ""
        for i in range(1, mLen):
            message += random.choice(words) + ""
        sendM(message=message)
        n += 1
        if n == 100:
            time.sleep(random.randint(60*60*3, 60*60*4))
        else:
            time.sleep(random.randint(30, 200))