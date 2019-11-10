from twython import Twython
from datetime import date
import datetime as time
from time import sleep
from threading import Thread
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
from defs import getMonth

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


def func():
    now = time.datetime.now()

    yearint = now.year
    monthint = now.month
    dayint = now.day
    
    d0 = date(yearint, monthint, dayint)
    d1 = date(2020, 8, 20)
    delta = d1 - d0
    print(delta.days)
    delta_str = str(delta.days)
    finalMessage = "There are " + delta_str + " days till my birthday"
    print("Tweeted: "+finalMessage)
    twitter.update_status(status=finalMessage)
    


if __name__ == '__main__':

    Thread(target = func).start()
    while True:
        sleep(86400)
        Thread(target = func).start()