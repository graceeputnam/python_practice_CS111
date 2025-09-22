import sys
import requests
import bs4


def scavenger_hunt(url, html_element, attribute):
    r = requests.get(url).text
    soup_object = bs4.BeautifulSoup(r, features="html.parser")
    tags = soup_object.find_all(html_element, attribute is True)
    for tag in tags:
        if tag.get(attribute) is not None:
            dog = tag.get(attribute)
    if attribute == "final":
        return dog
    else:
        attribute_list = dog.split(",")
        return scavenger_hunt(attribute_list[0], attribute_list[1], attribute_list[2])


def main(url, html_element, attribute, output):
    text = scavenger_hunt(url, html_element, attribute)
    with open(output, "w") as file:
        file.write(text)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

