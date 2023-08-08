import requests as r, random
from bs4 import BeautifulSoup as bs

__version__ = '1.0.0'

class ugent:
    def __init__(self):
        self.host = 'https://www.useragentstring.com/pages/'

    def ChromePlus(self, result = []):
        if len(result) == 0:
            web = bs(r.get(self.host + 'ChromePlus/').text, 'html.parser')
            for tag in web.find_all('a', href=lambda href: href and '/ChromePlus' in href):
                result.append(tag.text)
        
        ugent = random.choice(result)
        return ugent
