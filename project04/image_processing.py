import sys
from byuimage import Image


def darken(filename, percent):
    """*** YOUR CODE HERE ***"""
    image = Image(filename)
    for y in range(image.height):
        for x in range(image.width):
            new = image.get_pixel(x, y)
            new.red = new.red * (1 - percent)
            new.green = new.green * (1 - percent)
            new.blue = new.blue * (1 - percent)
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


def make_borders(filename, thickness, red, green, blue):
    image = Image(filename)
    new_image = Image.blank((image.width + (thickness * 2)), (image.height + (thickness * 2)))
    for y in range(0, new_image.height):
        for x in range(0, new_image.width):
            new = new_image.get_pixel(x, y)
            new.red = red
            new.green = green
            new.blue = blue
    for y in range(0, image.height):
        for x in range(0, image.width):
            old = image.get_pixel(x, y)
            new = new_image.get_pixel(x + thickness, y + thickness)
            new.red = old.red
            new.green = old.green
            new.blue = old.blue
    return new_image


def flipped(filename):
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    for y in range(0, image.height):
        for x in range(0, image.width):
            old = image.get_pixel(x, y)
            new = new_image.get_pixel(x, (image.height - y - 1))
            new.red = old.red
            new.green = old.green
            new.blue = old.blue
    return new_image


def mirror(filename):
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    for y in range(0, image.height):
        for x in range(0, image.width):
            old = image.get_pixel(x, y)
            new = new_image.get_pixel((image.width - x - 1), y)
            new.red = old.red
            new.green = old.green
            new.blue = old.blue
    return new_image


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


def rewrite_image(old_image, image, x_coord, y_coord):
    for y in range(0, image.height):
        for x in range(0, image.width):
            old = image.get_pixel(x, y)
            new = old_image.get_pixel(x_coord + x, y_coord + y)
            new.red = old.red
            new.green = old.green
            new.blue = old.blue
    return old_image


def collage(image1, image2, image3, image4, thickness):
    i_1 = Image(image1)
    i_2 = Image(image2)
    i_3 = Image(image3)
    i_4 = Image(image4)
    new_image = Image.blank(((i_1.width * 2) + (thickness * 3)), ((i_1.height * 2) + (thickness * 3)))
    for y in range(0, new_image.height):
        for x in range(0, new_image.width):
            new = new_image.get_pixel(x, y)
            new.red = 0
            new.green = 0
            new.blue = 0
    x_pixels = [thickness, (i_1.width + (thickness * 2))]
    y_pixels = [thickness, (i_1.height + (thickness * 2))]
    new_image = rewrite_image(new_image, i_1, x_pixels[0], y_pixels[0])
    new_image = rewrite_image(new_image, i_2, x_pixels[1], y_pixels[0])
    new_image = rewrite_image(new_image, i_3, x_pixels[0], y_pixels[1])
    new_image = rewrite_image(new_image, i_4, x_pixels[1], y_pixels[1])
    return new_image


def detect_green(pixel, i_threshold, i_factor):
    factor = i_factor
    threshold = i_threshold
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False


def green_screen(foreground, background, threshold, factor):
    back_image = Image(background)
    image = Image(foreground)
    for y in range(0, image.height):
        for x in range(0, image.width):
            old = back_image.get_pixel(x, y)
            new = image.get_pixel(x, y)
            if detect_green(new, threshold, factor):
                new.red = old.red
                new.green = old.green
                new.blue = old.blue
    return image


def show_image(filename):
    image = Image(filename)
    image.show()


def validate_commands(arguments):
    if arguments[1] == "-d" and len(arguments) >= 3:
        show_image(arguments[2])
        return True
    if arguments[1] == "-k" and len(arguments) == 5:
        image = darken(arguments[2], float(arguments[4]))
        image.save(arguments[3])
        return True
    if arguments[1] == "-s" and len(arguments) == 4:
        image = sepia(arguments[2])
        image.save(arguments[3])
        return True
    if arguments[1] == "-g" and len(arguments) == 4:
        image = grayscale(arguments[2])
        image.save(arguments[3])
        return True
    if arguments[1] == "-b" and len(arguments) == 8:
        image = make_borders(arguments[2], int(arguments[4]), int(arguments[5]), int(arguments[6]), int(arguments[7]))
        image.save(arguments[3])
        return True
    if arguments[1] == "-f" and len(arguments) == 4:
        image = flipped(arguments[2])
        image.save(arguments[3])
        return True
    if arguments[1] == "-m" and len(arguments) == 4:
        image = mirror(arguments[2])
        image.save(arguments[3])
        return True
    if arguments[1] == "-c" and len(arguments) == 8:
        image = collage(arguments[2], arguments[3], arguments[4], arguments[5], int(arguments[7]))
        image.save(arguments[6])
        return True
    if arguments[1] == "-y" and len(arguments) == 7:
        image = green_screen(arguments[2], (arguments[3]), float(arguments[5]), float(arguments[6]))
        image.save(arguments[4])
        return True
    else:
        return False


def main(arguments):
    print(arguments)
    if validate_commands(arguments):
        print("Valid input")
    else:
        raise TypeError('Invalid input')


if __name__ == "__main__":
    main(sys.argv[:])
