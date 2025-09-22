import requests
import bs4


def download(url, output_filename):
    """*** YOUR CODE HERE ***"""
    response_object = requests.get(url)
    text = response_object.text
    with open(output_filename, "w") as file:
        file.write(text)


def make_pretty(url, output_filename):
    """*** YOUR CODE HERE ***"""
    r = requests.get(url)
    soup_object = bs4.BeautifulSoup(r.text, features="html.parser")
    pretty = soup_object.prettify()
    with open(output_filename, "w") as file:
        file.write(pretty)


def find_paragraphs(url, output_filename):
    """*** YOUR CODE HERE ***"""
    r = requests.get(url)
    soup_object = bs4.BeautifulSoup(r.text, features="html.parser")
    list_of_tags = soup_object.find_all('p')
    tags = []
    for item in list_of_tags:
        tags.append(str(item))
        tags.append("\n")
    with open(output_filename, "w") as file:
        file.writelines(tags)


def find_links(url, output_filename):
    """*** YOUR CODE HERE ***"""
    r = requests.get(url)
    soup_object = bs4.BeautifulSoup(r.text, features="html.parser")
    list_of_hrefs = soup_object.find_all('a', href=True)
    websites = []
    for website in list_of_hrefs:
        href = website.get("href")
        websites.append(str(href).strip() + "\n")
    with open(output_filename, "w") as file:
        file.writelines(websites)
