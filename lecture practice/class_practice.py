class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def boost(self, amount):
        self.health += amount

    def damage(self, damage):
        self.health -= damage


#TREES
def print_tree(t, indent=0):
    print(indent * " " + str(t.label()))
    for b in t.branches():
        print_tree(b, indent + 2)

3
  1
  2
    1
    1





#extracting a table from webpage and creating a dictionary with keys as
#column names and the rest as the data in the column

def get_table(text):
    table = soup.find_all("table", id='degrees')[0]
    rows = soup.find_all("tr")
    headers_data = rows[0].find_all("th")
    headers = []
    for h in headers_data:
        headers.append(h.string)
    data = {}
    for name in headers:
        data[name] = []
    for row in rows[1:]:
        row_data = row.find_all("td")
        count = 0
        for item in row_data:
            value = item.string
            if count:
                value = int(value)
            data[headers[count]].append(value)
            count += 1
    return data


# how to find the urls to images on a page


