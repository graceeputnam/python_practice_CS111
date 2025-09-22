from byuimage import Image
# IMPORTANT - Remember to import Image from the byuimage library: `from byuimage import Image`


def iron_puzzle(filename):
    """*** YOUR CODE HERE ***"""
    image = Image(filename)
    for y in range(image.height):
        for x in range(image.width):
            new = image.get_pixel(x,y)
            new.red = 0
            new.green = 0
            new.blue = new.blue * 10
    return image


def west_puzzle(filename):
    """*** YOUR CODE HERE ***"""
    image = Image(filename)
    for y in range(image.height):
        for x in range(image.width):
            new = image.get_pixel(x, y)
            new.red = 0
            new.green = 0
            if new.blue < 16:
                new.blue = new.blue * 16
            else:
                new.blue = 0
    return image


def darken(filename, percent):
    """*** YOUR CODE HERE ***"""
    image = Image(filename)
    for y in range(image.height):
        for x in range(image.width):
            new = image.get_pixel(x, y)
            new.red = new.red * (1-percent)
            new.green = new.green * (1-percent)
            new.blue = new.blue * (1-percent)
    return image


def grayscale(filename):
    """*** YOUR CODE HERE ***"""
    image = Image(filename)
    for y in range(image.height):
        for x in range(image.width):
            new = image.get_pixel(x, y)
            average = (new.red + new.green + new.blue) / 3
            new.red = average
            new.green = average
            new.blue = average
    return image


def sepia(filename):
    """*** YOUR CODE HERE ***"""
    image = Image(filename)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
            true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
            true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
            if pixel.red > 255:
                pixel.red = 255
            else:
                pixel.red = true_red
            if pixel.green > 255:
                pixel.green = 255
            else:
                pixel.green = true_green
            if pixel.blue > 255:
                pixel.blue = 255
            else:
                pixel.blue = true_blue
    return image


def create_left_border(filename, weight):
    """*** YOUR CODE HERE ***"""
    image = Image(filename)
    new_image = Image.blank(image.width + weight, image.height)
    for y in range(new_image.height):
        for x in range(new_image.width):
            n = new_image.get_pixel(x, y)
            n.red = 0
            n.green = 0
            n.blue = 255
    for y in range(image.height):
        for x in range(image.width):
            old = image.get_pixel(x, y)
            new = new_image.get_pixel(x + weight, y)
            new.red = old.red
            new.green = old.green
            new.blue = old.blue
    return new_image


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    """*** YOUR CODE HERE ***"""


def copper_puzzle(filename):
    """*** YOUR CODE HERE ***"""

