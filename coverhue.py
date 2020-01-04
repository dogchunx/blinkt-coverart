import urllib.request
import requests
import time
import json
import blinkt
from colorthief import ColorThief

lastAlbum = ''
brightness = 0.9

blinkt.set_clear_on_exit

blinkt.set_all(0, 255, 0)

blinkt.show()

while True:

    req = requests.get(
        url = 'https://api.spotify.com/v1/me/player/currently-playing', 
        headers={   'content-type': 'application/json', 
                    'accept': 'application/json',
                    'Authorization': 'Bearer BQCkwTJTwdT9B155T8e3s1DhVxJ58hkaXkvlnmpU8i6gjSuRwFmzMWeK8nBNR5k9gRHp9CQesH9fM3dwTdffAM1JK79k8afEuLGobxrkwNYlaEAwykyr4XGr5vEdLM-pWPWzQKgcMg-lICZZAw'})

    if req.status_code == 200:

        data = json.loads(req.text)
        
        coverUrl = data["item"]["album"]["images"][0]["url"]
        currentAlbum = data["item"]["album"]["name"]
        artistName = data["item"]["artists"][0]["name"]
                    
        print(artistName + ': ' + currentAlbum)

        if currentAlbum != lastAlbum:

            urllib.request.urlretrieve(coverUrl, 'image.jpg')

            color_thief = ColorThief('image.jpg')

            dominant_colors = color_thief.get_palette(color_count = 9, quality=10)

            count = 0

            while count <= 7:
                currentColour = dominant_colors[count]
                print(currentColour)
                blinkt.set_pixel(count, currentColour[0], currentColour[1], currentColour[2], brightness)
                count = count + 1

            #blinkt.set_all(dominant_color[0], dominant_color[1], dominant_color[2], 0.9)

            blinkt.show()

            #print(dominant_color)
        else:
            print('not changed - skipping')
        lastAlbum = currentAlbum
    else:
        print(req)
        
    time.sleep(5)