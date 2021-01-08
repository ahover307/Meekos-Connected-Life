from gpiozero import Button
import json
import requests
from time import sleep


PIN = 17

def make_request():
    url = "https://api.pushbullet.com/v2/pushes"
    headers = {
        "Access-Token": "",
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "type": "note",
        "title": "Meeko!",
        "body": "Meeko is ready to come inside!",
        "channel_tag": "meekos-connected-life"
    })

    r = requests.post(url, headers=headers, data=data)
    if json.loads(r.text) == {}:
        return 'Good Response'
    else:
        return 'Bad Response'


button = Button(PIN)
while True:
    button.wait_for_press()
    print(make_request())
    sleep(60)

print(make_request())
