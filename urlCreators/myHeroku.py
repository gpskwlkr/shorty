from urlCreators.checkURL import check
import requests

class Heroku():
    def __init__(self):
        self._base = 'https://flaskshortener.herokuapp.com/api/v1/'

    def getShortUrl(self, url):
        url = check(url)
        return requests.post(self._base, json={"url" : url}).json()['url']

heroku = Heroku()