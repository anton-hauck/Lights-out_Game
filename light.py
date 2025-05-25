

class light:
    def __init__(self, position_x, position_y, on = False, neighbours = None):
        self.position_x = position_x
        self.position_y = position_y
        self.on = on
        self.neighbours = []

    def switch(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    def switched(self):
        for neighbour in self.neighbours:
            neighbour.switch()

    def __repr__(self):
        return f"{self.position_x},{self.position_y},{self.on}"