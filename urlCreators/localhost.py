from urlCreators.checkURL import check
import requests
import json

class Local():
    def __init__(self):
        self.baseURL = 'http://localhost:5000/api/'

    def getShortUrl(self, url):
        if url[:8] != 'https://' or url[:7] != 'http://':
            url = check(url)
        return json.loads(requests.post(self.baseURL, params = {'url' : url}).text)

local = Local()