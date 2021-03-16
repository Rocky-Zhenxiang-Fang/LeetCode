class Codec:
    def __init__(self):
        self.hash_url = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:
            value = "http://" + self.hash()
            if value not in self.hash_url:
                self.hash_url[value] = longUrl
                return value

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash_url[shortUrl]


    def hash(self) -> str:
        import random
        res = []
        while len(res) < 6:
            res.append(chr(random.randrange(0, 255)))
        return "".join(res)