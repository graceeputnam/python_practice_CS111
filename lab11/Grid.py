

class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [[None for k in range(width)] for i in range(height)]

    def in_bounds(self, x, y):
        if 0 > x or x > self.width or 0 > y or y > self.height:
            raise IndexError
        else:
            return True

    def get(self, x, y):
        if 0 > x or x > self.width or 0 > y or y > self.height:
            raise IndexError
        print(self.array[y][x])
        return self.array[y][x]

    def set(self, x, y, val):
        if 0 > x or x > self.width or 0 > y or y > self.height:
            raise IndexError
        self.array[y][x] = val

    def __str__(self):
        return f"Grid({self.width}, {self.height}, first = {self.array[0][0]})"

    def __repr__(self):
        return f"Grid({self.width}, {self.height}, first = {self.array[0][0]})"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        else:
            return False