import string
import random
class Codec:

    pairs = {}

    def encode(self, longUrl: str) -> str:
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 5))
        Codec.pairs[random_string] = longUrl
        return "https://tinyurl.com/" + random_string
        """
        Encodes a URL to a shortened URL.
        """
        

    def decode(self, shortUrl: str) -> str:
        """
        Decodes a shortened URL to its original URL.
        """
        code = shortUrl[-5:]
        print(code)
        return Codec.pairs[code]

test = Codec()
shortened_url = test.encode("https://github.com/")
print(test.decode(shortened_url))
