import sys


def read_file(info):
    new_list = []
    with open(info, "r") as file:
        lines = file.readlines()
    for line in lines:
        new_list.append(line)
    return new_list


def write_list(output, lst):
    with open(output, "w") as file:
        file.writelines(lst)


def merge_lists(list_1, list_2):
    new_list = []
    while list_1 and list_2:
        if list_1[0] <= list_2[0]:
            new_list.append(list_1[0])
            list_1 = list_1[1:]
        else:
            new_list.append(list_2[0])
            list_2 = list_2[1:]
    if list_1:
        new_list.extend(list_1)
    if list_2:
        new_list.extend(list_2)
    return new_list


def sort_list(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid_point = len(unsorted_list) // 2
    left = unsorted_list[:mid_point]
    right = unsorted_list[mid_point:]
    left = sort_list(left)
    right = sort_list(right)
    return merge_lists(left, right)


def main(file, output):
    lst = read_file(file)
    sorted = sort_list(lst)
    write_list(output, sorted)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])