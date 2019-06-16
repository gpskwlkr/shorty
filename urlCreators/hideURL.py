import json
import requests
from urlCreators.checkURL import check 

class Hide():
    def __init__(self):
        self._base = 'https://hideuri.com/api/v1/shorten'

    def getShortUrl(self, url):
        url = check(url)
        return json.loads(requests.post(self._base, {'url' : url}).content)['result_url']

hide = Hide()