import requests as r, random
from bs4 import BeautifulSoup as bs

class ugent:
    def __init__(self):
        self.source = bs(r.get('https://www.useragentstring.com/pages/Browserlist/').text, 'html.parser')
        self.useragent = self.get_browser_name()
        self.get_ua()

    def get_browser_name(self):
        result = {}
        for x in self.source.find_all('img', {'class':'uaIcon', 'alt':True}):
            result.update({x['alt']:[]})

        return result

    def get_ua(self):
        for key in self.useragent:
            result = []
            for ua in self.source.find_all('a', href=lambda href: href and '/'+key in href):
                result.append(ua.text)
            self.useragent[key] = result
    
    def random(self, count=1, combine=[]):
        for value in self.useragent.values():
            combine.extend(value)

        result = random.sample(combine, int(count))
        return result

    def browser(self, name = 'Chrome'):
        result = random.choice(self.useragent[name])
        return result
        
