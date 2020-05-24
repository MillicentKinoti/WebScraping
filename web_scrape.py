from bs4 import  BeautifulSoup
import  requests
url = 'https://automatetheboringstuff.com/'
raw_html = requests.get(url)

html= BeautifulSoup(raw_html.text, 'html.parser')
for i, li  in enumerate(html.select('li')):
    print((i, li.text))

#enumerate function adss a counter as the key of the enumerate object