from byuimage import Image


def flipped(filename):
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    for y in range(0, image.height):
        for x in range(0, image.width):
            old = image.get_pixel(x,y)
            new = new_image.get_pixel(x, (image.height-y-1))
            new.red = old.red
            new.green = old.green
            new.blue = old.blue
    return new_image


def make_borders(filename, thickness, red, green, blue):
    image = Image(filename)
    new_image = Image.blank((image.width + (thickness*2)), (image.height + (thickness*2)))
    for y in range(0,new_image.height):
        for x in range(0, new_image.width):
            new = new_image.get_pixel(x,y)
            new.red = red
            new.green = green
            new.blue = blue
    for y in range(0 ,image.height):
        for x in range(0, image.width):
            old = image.get_pixel(x,y)
            new = new_image.get_pixel(x + thickness,y + thickness)
            new.red = old.red
            new.green = old.green
            new.blue = old.blue
    return new_image



if __name__ == "__main__":
    pass
