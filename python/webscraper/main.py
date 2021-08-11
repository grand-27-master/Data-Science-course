from bs4 import BeautifulSoup
import requests

search = input('search here:')
params = {'q': search}
r = requests.get('https://www.bing.com/search', params=params)

soup = BeautifulSoup(r.text, 'html.parser')  # to remove parser warning
print(soup.prettify())  # prints text form of a web page
result = soup.find('ol', {'id': 'b_result'})
link = result.findAll('li', {'class': 'b_algo'})

for item in link:
    item_text = item.find('a').text  # shows text of that element
    item_href = item.find('a').attrs['href']  # shows URL of that element

    if item_text and item_href:
        # extracts data of pizza website
        print('text:', item_text)
        print('URL:', item_href)
        print('parent:', item.find('a').parent)
