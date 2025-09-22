def even_weighted(s):
    new_list = []
    for i in range(len(s)):
        if i % 2 == 0:
            new_list.append(s[i]*i)
    return new_list


def couple(s, t):
    new_list = []
    for i in range(len(s)):
        new_list.append([s[i], t[i]])
    return new_list


def copy_file(input_filename, output_filename):
    with open(input_filename,"r") as file:
        lines = file.readlines()
        counter = 1
        for line in lines:
            with open(output_filename, "a") as output:
                output.write(f"{counter}: ")
                output.write(line)
            counter += 1


########################################################
# OPTIONAL QUESTIONS


def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    """*** YOUR CODE HERE ***"""
