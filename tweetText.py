
from twython import Twython
import datetime as time
from defs import getMonth
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

now = time.datetime.now()

yearint = now.year
month_str = getMonth(now.month)
dayint = now.day

year_str = str(yearint)
day_str = str(dayint)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = input("What do you want to Tweet? ")
finalMessage = "This was Tweeted automaticaly on " + month_str + " " + day_str + ", " + year_str + ": " + message
print(finalMessage)
twitter.update_status(status=finalMessage)