from Grid import Grid

class Particle:
    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.x = x
        self.y = y

    def __str__(self):
        return f"{type(self).__name__}({self.x},{self.y})"

    def physics(self):
        pass

    def move(self):
        position = self.physics()
        if position is None:
            return
        else:
            self.grid.set(self.x, self.y, None)
            self.x = position[0]
            self.y = position[1]
            self.grid.set(position[0], position[1], self)

