
from urllib.parse import urlparse, urljoin
import requests


# *WRITE YOUR CODE IN THIS FILE*
def get_domain(url):
    parsed = urlparse(url)
    scheme = parsed.scheme
    netloc = parsed.netloc
    if str(scheme) == "http" or str(scheme) == "https" and netloc != "":
        return str(scheme) + "://" + str(netloc)
    else:
        return ""


def combine_paths(url, path):
    return urljoin(url, path)


def combine_urls(base, join):
    return urljoin(base, join)


def print_pages(url, path_pages, output):
    current_path = url
    for path in path_pages:
        current_path = combine_paths(current_path, path)
        response_object = requests.get(current_path)
        text = response_object.text
        with open(output, "a") as file:
            file.write(text)
            file.write("\n")
