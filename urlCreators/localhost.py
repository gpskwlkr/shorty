from urlCreators.checkURL import check
import requests
import json

class Local():
    def __init__(self):
        self._base = 'http://localhost:5000/api/v1/'

    def getShortUrl(self, url):
        url = check(url)
        return requests.post(self._base, json={"url" : url}).json()['url']

local = Local()