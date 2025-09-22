import random


def exception_maker():
    raise TypeError


# QUESTION 1:
def exception_handler():
    """ Write a function that uses a try-except block to handle an exception.
    If an exception is thrown/raised, then print out something like:
    "Exception caught! Exception type: <<put the type of the exception here>>"
    """
    """*** YOUR CODE HERE ***"""
    try:
        exception_maker()
    except Exception as e:
        print(f'Exception caught! Exception type: {type(e)}')


# QUESTION 2:
def in_range1(n):
    """ Write a function that checks to see if n is
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    >>> in_range1(103)
    False
    """
    """*** YOUR CODE HERE ***"""
    if 100 >= n >= 1:
        return True
    else:
        return False


# QUESTION 3:
def in_range2(n):
    """ Redo in_range1, but instead of returning False, raise a ValueError
    if n is outside the range of 1-100.
    """
    """*** YOUR CODE HERE ***"""
    if 100 >= n >= 1:
        return True
    else:
        raise ValueError


def main():
    """ Write code in the main function that generates 1000
    random numbers between 1 and 101 and calls both in_range1
    and in_range2 function to validate the numbers generated using
    both functions.
    """
    """*** YOUR CODE HERE ***"""
    random_numbers = [random.randint(1, 101) for i in range(1000)]
    for i in random_numbers:
        if in_range1(i):
            continue
        else:
            print(f"{i} failed the validation function in_range1")
        try:
            in_range2(i)
        except ValueError:
            print(f"{i} failed the validation function in_range2")


# QUESTION 4:
def bound_checker(x_dimension, y_dimension, x, y):
    """ If given an x and a y dimension which represent the maximum values on a grid
    (think of a square with dimensions x = 10, y = 12, for example),
    write a function that returns True if the x and y are within the grid,
    and throws an IndexError if they are out of bounds.
    >>> bound_checker(10, 12, 2, 3)
    True
    >>> bound_checker(10, 12, 59, 3)
    Traceback (most recent call last):
        ...
    IndexError
    """
    """*** YOUR CODE HERE ***"""
    if 0 < x < x_dimension and 0 < y < y_dimension:
        return True
    else:
        raise IndexError


# QUESTION 5 (OPTIONAL):
def validate_age(user_input):
    """ Try and convert the user_input to be an integer, check to see if the age is between 0 and 123,
    and return that integer. If the age is out of the accepted age range, raise a value error
    with the message "Age outside range!"
    """
    """*** YOUR CODE HERE ***"""


def handle_user_input():
    """ Prompt the user for an input of only numbers (no letters or special characters).
    Then call validate_age() to change that input to an integer. Handle any errors that
    might be generated using a try/except block. If you catch/except a ValueError, print out something like:
    "Invalid Age: {user_input}. contains non-numerical characters!"
    """
    """*** YOUR CODE HERE ***"""
