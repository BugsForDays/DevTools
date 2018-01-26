
from bs4 import BeautifulSoup
import requests
import pprint
url = 'https://whatismyipaddress.com/ip/73.222.68.248'

pp = pprint.PrettyPrinter(indent=4)

header = {'user-Agent':'curl/7.21.3'}

r = requests.get(url,header).content

soup = BeautifulSoup(r, 'html.parser')
# pp.pprint(soup.findAll('th'))
for head, data in zip(soup.findAll('th'), soup.findAll('td')):
    print(head.text.strip() + " " + data.text.strip())
