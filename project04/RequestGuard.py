import requests
import re
from urllib.parse import urlparse


class RequestGuard:
    def parse_robots(self):
        text = (requests.get('https://' + self.domain + "/robots.txt")).text
        return re.findall("Disallow: (.*)" ,text)

    def __init__(self, url):
        self.url = url
        self.domain = urlparse(url).netloc
        self.forbidden = self.parse_robots()

    def can_follow_link(self, url):
        if not self.domain in url:
            return False
        else:
            path = urlparse(url).path
            for item in self.forbidden:
                if path.startswith(item):
                    return False
            return True

    def make_get_request(self, link, use_stream=False):
        if self.can_follow_link(link) is True:
            return requests.get(link, stream=use_stream)
        else:
            return None



def main():
    pass

if __name__ == "__main__":
    main()