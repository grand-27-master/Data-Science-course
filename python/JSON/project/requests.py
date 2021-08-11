# import requests  # library used to send all kinds of requests to HTTP
#
# r = requests.get("http://google.com")
# print('status:', r.status_code)   # displays code:200, its like getting 404 or any other code which signifies status of web page and 200 means web page is ok
# print('URL:', r.url)
#

import requests
from io import BytesIO
from PIL import Image  # image processing library(pillow)

r = requests.get(
    'https://www.google.com/url?sa=i&url=https%3A%2F%2Fhelpx.adobe.com%2Fstock%2Fhow-to%2Fvisual-reverse-image-search.html&psig=AOvVaw03zI42gYz2S457Gb9QLqhY&ust=1589004067719000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKi4gsvLo-kCFQAAAAAdAAAAABAD')
print('status code:', r.status_code)

img = Image.open(BytesIO(r.content))
path = './img.jpg'
print(img.size, img.format, img.mode)
