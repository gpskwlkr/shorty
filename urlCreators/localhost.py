from urlCreators.checkURL import check
import requests
import json

class Local():
    def __init__(self):
        self.baseURL = 'http://localhost:5000/api/'

    def getShortUrl(self, url):
        url = check(url)
        print(url)
        return requests.post('http://localhost:5000/api/v1/', json={"url" : url}).json()['url']

local = Local()