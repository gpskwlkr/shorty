from urlCreators.checkURL import check
import requests

class Tiny():
    def __init__(self):
        self.baseURL = 'http://tinyurl.com/api-create.php'

    def getShortUrl(self, url):
        if url[:8] != 'https://' or url[:7] != 'http://':
            url = check(url)
        return requests.post(self.baseURL, {'url' : url}).text

tinyurl = Tiny()