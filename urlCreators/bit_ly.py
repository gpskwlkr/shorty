from urlCreators.checkURL import check 
import requests

class Bit():
    def __init__(self):
        self._base = 'http://tinyurl.com/api-create.php'

    def getShortUrl(self, url):
        if url[:8] != 'https://' or url[:7] != 'http://':
            url = check(url)
        return requests.post(self.baseURL, {'url' : url}).text



bit = Bit()