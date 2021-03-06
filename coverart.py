import urllib.request
import requests
import time
import json
import blinkt
from colorthief import ColorThief

lastAlbum = ''

blinkt.set_clear_on_exit

blinkt.set_all(0, 255, 0)

blinkt.show()

while True:

    req = requests.get(
        url = 'https://api.spotify.com/v1/me/player/currently-playing', 
        headers={   'content-type': 'application/json', 
                    'accept': 'application/json',
                    'Authorization': 'Bearer [TOKEN]'})

    if req.status_code == 200:

        data = json.loads(req.text)
        
        coverUrl = data["item"]["album"]["images"][0]["url"]
        currentAlbum = data["item"]["album"]["name"]
        artistName = data["item"]["artists"][0]["name"]
                    
        print(artistName + ': ' + currentAlbum)

        if currentAlbum != lastAlbum:

            urllib.request.urlretrieve(coverUrl, 'image.jpg')

            color_thief = ColorThief('image.jpg')

            dominant_color = color_thief.get_color(quality=10)

            blinkt.set_all(dominant_color[0], dominant_color[1], dominant_color[2], 0.9)

            blinkt.show()

            print(dominant_color)
        else:
            print('not changed = skipping')
        lastAlbum = currentAlbum
    else:
        print(req)
        
    time.sleep(5)
