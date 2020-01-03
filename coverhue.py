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
                    'Authorization': 'Bearer BQCxTudro89XG4qAVSwJVSz3TGO_eGIy9hJY7uxDV4BGysFTtLhwYctm9K1J9iLAOrb9PHxs3xovie49gsloxML-D6FSTtcMvKRirA9U5hmkkUrT1OaHD8xdN63fJVOBWLXiZy6YzXKbRvWRDA'})

    if req.status_code == 200:

        data = json.loads(req.text)
        
        coverUrl = data["item"]["album"]["images"][0]["url"]

        print(data["item"]["artists"][0]["name"] + ': ' + data["item"]["album"]["name"])

        urllib.request.urlretrieve(coverUrl, 'image.jpg')

        color_thief = ColorThief('image.jpg')

        dominant_color = color_thief.get_color(quality=1)

        print(dominant_color)
    else:
        print(req)
        
    time.sleep(5)