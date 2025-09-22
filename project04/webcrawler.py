import sys
import bs4
from RequestGuard import RequestGuard, requests
from image_processing import sepia, grayscale, mirror, flipped
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import matplotlib.pyplot as plt
import re


def count_links(url, output_1, output_2):
    links_to_visit = []
    guard = RequestGuard(url)
    links_to_visit.append(url)
    link_counts = {}
    while links_to_visit:
        popped = links_to_visit.pop(0)
        if popped in link_counts:
            link_counts[popped] += 1
        else:
            link_counts[popped] = 1
            if guard.can_follow_link(popped):
                page = guard.make_get_request(popped)
                html = BeautifulSoup(page.text,"html.parser")
                for tag in html.find_all('a'):
                    href = tag.get('href')
                    new_url = urljoin(popped, href.split("#")[0])
                    links_to_visit.append(new_url)
    generate_plot(links_to_visit, link_counts, output_1, output_2)


def generate_plot(links_to_visit, dictionary, output_1, output_2):
    value = [value for value in dictionary.values()]
    bin_counts, bin_nums, item = plt.hist(value, bins=range(min(value), max(value) + 2))
    plt.savefig(output_1) #output 1
    plt.clf()
    with open(output_2, "w") as file:
        for i in range(len(bin_counts)):
            file.write(f"{bin_nums[i]},{bin_counts[i]}\n")


def plot_data(argv):
    url = argv[2]
    website = requests.get(url)
    if website.status_code != 200:
        print("Bad website")
    else:
        soup = bs4.BeautifulSoup(website.text, "html.parser")
        table = soup.find_all("table", id='CS111-Project4b')[0]
        data = []
        rows = table.find_all("tr")
        for i in range(len(rows[0].find_all("td"))):
            data.append([])
        for row in rows:
            columns = row.find_all("td")
            index = 0
            for col in columns:
                data[index].append(float(col.string))
                index += 1
        colors = ["b", "g", "r", "k"]
        for i in range(1, len(data)):
            plt.plot(data[0], data[i], color=colors[i-1])
        plt.savefig(argv[3])
        with open(argv[4], "a") as file:
            for i in range(len(data[0])):
                string = ""
                for j in range(len(data)):
                    string += f"{data[j][i]},"
                string = string.strip(",")
                string += "\n"
                file.write(string)
        plt.clf()


def find_image(url, prefix, command):
    image_list = []
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    images = soup.find_all("img")
    for tag in images:
        src = tag.get('src')
        new_src = urljoin(url, src.split("#")[0])
        image_list.append(new_src)
    for link in image_list:
        output = link.split("/")[-1]
        with open(output, "wb") as file:
            guard = RequestGuard(link)
            response = guard.make_get_request(link)
            file.write(response.content)
        new_output = f"{prefix}{output}"
        if command == "-s":
            new_image = sepia(output)
        elif command == "-g":
            new_image = grayscale(output)
        elif command == "-f":
            new_image = flipped(output)
        elif command == "-m":
            new_image = mirror(output)
        new_image.save(new_output)


if __name__ == "__main__":
    if len(sys.argv) >= 4:
        first_flag = sys.argv[1]
        if first_flag == "-c":
            count_links(sys.argv[2], sys.argv[3], sys.argv[4])
        elif first_flag == "-p":
            plot_data(sys.argv)
        elif first_flag == "-i":
            image_flag = sys.argv[4]
            if image_flag == "-s": #sepia
                find_image(sys.argv[2], sys.argv[3], sys.argv[4])
            if image_flag == "-g": #greyscale
                find_image(sys.argv[2], sys.argv[3], sys.argv[4])
            if image_flag == "-f": #vertical-flip
                find_image(sys.argv[2], sys.argv[3], sys.argv[4])
            if image_flag == "-m": #horizontal-flip
                find_image(sys.argv[2], sys.argv[3], sys.argv[4])
            else:
                print("Invalid arguments")
            pass
        else:
            print('Invalid arguments')
    else:
        print("Invalid arguments")
