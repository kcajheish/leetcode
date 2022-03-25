from collections import defaultdict
class Codec:
    """
    1. index long url as tiny
    2. randomly generate short url from a-zA-Z0-9
    3. hash code
    """
    short = defaultdict()
    long = defaultdict()
    host = 'http://tinyurl.com/'
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.short:
            tiny = f"{self.host}{hash(longUrl)}"
            self.short[longUrl] = tiny
            self.long[tiny] = longUrl
        return self.short[longUrl]


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.long[shortUrl]
