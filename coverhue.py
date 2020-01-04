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
                    'Authorization': 'Bearer BQAlu96QX1k4DTDZdlACRJtSaOnTRti3_xB4v2tmA--4tkcJc5AeKGc67SzuQ3z6pSJXdo9_0CtAZt2SKEpHYVg88OUwAS86Bx0lVmLD3cmq21BLVKRh2_GAuonkyAZTZGzR40pX6_vllM69tw'})

    if req.status_code == 200:

        data = json.loads(req.text)
        
        coverUrl = data["item"]["album"]["images"][0]["url"]
        currentAlbum = data["item"]["album"]["name"]
        artistName = data["item"]["artists"][0]["name"]
                    
        print(artistName + ': ' + currentAlbum)

        if currentAlbum != lastAlbum:

            urllib.request.urlretrieve(coverUrl, 'image.jpg')

            color_thief = ColorThief('image.jpg')

            dominant_colors = color_thief.get_palette(color_count = 8, quality=10)
            
            count = 0

            while count <= 7:
                blinkt.set_pixel(count, dominant_colors[count][0], dominant_colors[count][1], dominant_colors[count][1], 0.9)
                count = count + 1

            #blinkt.set_all(dominant_color[0], dominant_color[1], dominant_color[2], 0.9)

            blinkt.show()

            print(dominant_color)
        else:
            print('not changed = skipping')
        lastAlbum = currentAlbum
    else:
        print(req)
        
    time.sleep(5)