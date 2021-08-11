from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search = input('search here:')
params = {'q': search}
r = requests.get('https://www.bing.com/images/search', params=params)
soup = BeautifulSoup(r.text, 'html.parser')
link = soup.findAll('a', {'class': 'thumb'})

for item in link:
    img_obj = requests.get(item.attrs['href'])
    print('getting images:', item.attrs['href'])
    title = item.attrs['href'].split('/')[-1]  # to get last element
    img = Image.open(BytesIO(img_obj.content))  # opens an image
    img.save('./scraped_images/' + title, img.format)  # saving image in a directory
