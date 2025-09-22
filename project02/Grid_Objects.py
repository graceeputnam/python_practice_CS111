from Particle import Particle


class Sand(Particle):
    def is_move_ok(self, x, y):
        if x > self.grid.width - 1 or y > self.grid.height - 1 or y < 0 or x < 0:
            return False
        if self.grid.get(x, y) is not None:
            return False
        if x == self.x and self.grid.get(x, y) is None:
            return True
        if x != self.x:
            if x == (self.x - 1):
                if self.grid.get(x, y) is None and self.grid.get(x, y - 1) is None:
                    return True
            if x == (self.x + 1):
                if self.grid.get(x, y) is None and self.grid.get(x, y - 1) is None:
                    return True
        else:
            return False

    def physics(self):
        if self.is_move_ok(self.x, (self.y + 1)):
            place = (self.x, self.y + 1)
            return place
        elif self.is_move_ok(self.x - 1, (self.y + 1)):
            place = (self.x - 1, self.y + 1)
            return place
        elif self.is_move_ok(self.x + 1, (self.y + 1)):
            place = (self.x +1, self.y +1)
            return place
        else:
            return None


class Rock(Particle):
    def physics(self):
        return None


class Bubble(Particle):
    def is_move_ok(self, x, y):
        if x > self.grid.width - 1 or y > self.grid.height - 1 or y < 0 or x < 0:
            return False
        if self.grid.get(x, y) is not None:
            return False
        if x == self.x and self.grid.get(x, y) is None:
            return True
        if x != self.x:
            if x == (self.x - 1):
                if self.grid.get(x, y) is None and self.grid.get(x, y + 1) is None:
                    return True
            if x == (self.x + 1):
                if self.grid.get(x, y) is None and self.grid.get(x, y + 1) is None:
                    return True
        else:
            return False

    def physics(self):
        if self.is_move_ok(self.x, (self.y - 1)):
            place = (self.x, self.y - 1)
            return place
        elif self.is_move_ok(self.x + 1, (self.y - 1)):
            place = (self.x + 1, self.y - 1)
            return place
        elif self.is_move_ok(self.x - 1, (self.y - 1)):
            place = (self.x - 1, self.y - 1)
            return place
        else:
            return None
