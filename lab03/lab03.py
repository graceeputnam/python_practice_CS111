def average_temperature(temps):
    """
    Given a list of temperatures, TEMPS, compute the average
    temperature and return it to the user
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> average_temperature(temp_data)
    75.15
    """
    total = 0
    counter = 0
    for temp in temps:
        total += temp
        counter += 1
    return total/counter



def hot_days(temps):
    """
    Given a list of temperatures, TEMPS, count the number of days
    more than five degrees above the average.  Print the number of
    days and the average and return the number of days.
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> hot_days(temp_data)
    There were 2 day(s) more than 5 degrees above the average of 75.2.
    2
    """
    average = average_temperature(temps)
    count = 0
    for temp in temps:
        if temp >= average + 5:
            count += 1
    print(f"There were {count} day(s) more than 5 degrees above the average of {average:.1f}.")
    return count


def is_palindrome(word):
    """
    Given a single word, WORD, determine if it is a palindrome or not.
    Print a message that includes the word stating it is or is not a
    palindrome and return True if it is and False otherwise
    >>> is_palindrome('rotator')
    rotator is a palindrome.
    True
    >>> is_palindrome('apple')
    apple is not a palindrome.
    False
    """
    counter = 0
    for i in range(len(word)):
        if word[i] == word[-(i+1)]:
            continue
        else:
            counter += 1
    if counter == 0:
        print(f"{word} is a palindrome.")
        return True
    else:
        print(f"{word} is not a palindrome.")
        return False


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]