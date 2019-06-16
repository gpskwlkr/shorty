from urlCreators.checkURL import check
import requests

class Tiny():
    def __init__(self):
        self._base = 'http://tinyurl.com/api-create.php'

    def getShortUrl(self, url):
        url = check(url)
        return requests.post(self._base, {'url' : url}).text

tinyurl = Tiny()