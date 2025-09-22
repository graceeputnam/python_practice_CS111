from copy import deepcopy


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
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        else:
            return True

    def get(self, x, y):
        if Grid.in_bounds(self, x, y):
            return self.array[y][x]
        else:
            raise IndexError

    def set(self, x, y, val):
        if Grid.in_bounds(self, x, y):
            self.array[y][x] = val
        else:
            raise IndexError

    def __str__(self):
        return f"Grid({self.width}, {self.height}, first = {self.array[0][0]})"

    def __repr__(self):
        return f"Grid.build({self.array})"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        if isinstance(other, list):
            return self.array == Grid.build(other).array
        else:
            return False

    @staticmethod
    def check_list_malformed(lst):
        if lst is None:
            raise ValueError("Input must be a non-empty list of lists.")
        if not isinstance(lst, list):
            raise ValueError("Input must be a non-empty list of lists.")
        if lst == "" or lst == []:
            raise ValueError("List must not be empty")
        if len(lst) > 1:
            if not isinstance(lst[0], list):
                raise ValueError("Input must be a list of lists")
            length = len(lst[0])
            for item in lst:
                if not isinstance(item, list):
                    raise ValueError("Input must be a list of lists.")
                if not len(item) == length:
                    raise ValueError("All items in list must be lists of the same length.")
        else:
            raise ValueError("input must be a list of lists")

    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        grid = Grid(width, height)
        grid1 = deepcopy(grid)
        grid1.array = lst
        return grid1

    def copy(self):
        return self.build([[self.get(x, y) for x in range(self.width)] for y in range(self.height)])
