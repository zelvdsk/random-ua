import requests as r, random
from bs4 import BeautifulSoup as bs

class ugent:
    def __init__(self):
        self.host = 'https://www.useragentstring.com/pages/'

    def get_string(self, endpoint, patch):
        result = []
        web = bs(r.get(self.host + endpoint).text, 'html.parser')
        for tag in web.find_all('a', href=lambda href: href and patch in href):
            result.append(tag.text)

        return result
        
    def ChromePlus(self, ua=[]):
        if len(ua) == 0:ua.extend(self.get_string('ChromePlus/', '/ChromePlus'))
        
        acak = random.choice(ua)
        return acak

    def Chrome(self, ua=[]):
        if len(ua) == 0:ua.extend(self.get_string('Chrome/', '/Chrome'))

        acak = random.choice(ua)
        return acak

    def Firefox(self, ua=[]):
        if len(ua) == 0:ua.extend(self.get_string('Firefox/', '/Firefox'))
        
        acak = random.choice(ua)
        return acak
    
    def Opera(self, ua=[]):
        if len(ua) == 0:ua.extend(self.get_string('Opera/', '/Opera'))
        
        acak = random.choice(ua)
        return acak

    def Arora(self, ua=[]):
        if len(ua) == 0:ua.extend(self.get_string('Arora/', '/Arora'))
        
        acak = random.choice(ua)
        return acak

    
