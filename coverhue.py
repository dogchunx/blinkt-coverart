import urllib.request
import requests
import time
import json
from colorthief import ColorThief

while True:

    req = requests.get(
        url = 'https://api.spotify.com/v1/me/player/currently-playing', 
        headers={   'content-type': 'application/json', 
                    'accept': 'application/json',
                    'Authorization': 'Bearer BQDBWjyyFLb1_p2pofulhZMLxE8-1LfuMRQSM1i8AHi0M_j6YFqfTjVmvcI6Bh7F9OtCYDmiQeYpL8pzvwQGWEo4l3ExINyu0TInZqbgJoUPzrU7sSNx4pR250Imw0HgFXJBTdTuhqqsFaXrKg'})

    if req.status_code == 200:

        data = json.loads(req.text)
        
        coverUrl = data["item"]["album"]["images"][0]["url"]

        print(data["item"]["artists"][0]["name"] + ': ' + data["item"]["album"]["name"])

        urllib.request.urlretrieve(coverUrl, 'image.jpg')

        color_thief = ColorThief('image.jpg')

        dominant_color = color_thief.get_color(quality=1)

        print(dominant_color)
        
    time.sleep(5)