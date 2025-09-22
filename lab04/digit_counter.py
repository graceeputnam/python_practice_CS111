def even_digit_counter(num):
    """Return the number of even digits"""
    counter = 0
    while num > 0:
        current_digit = num % 10
        print(current_digit)
        if current_digit % 2 == 0:
            counter += 1
        num = num // 10
    return counter

"""ADD_TESTING_CODE"""


