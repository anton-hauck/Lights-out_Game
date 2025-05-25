from light import light


class light_manager:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.lights = []
        self.init_lights()
        self.init_neighbours()

    def init_lights(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.lights.append(light(row + 1, column + 1))

    def init_neighbours(self):
        for light in self.lights:
            for neighbour in self.lights:
                if light.position_x == neighbour.position_x - 1 and light.position_y == neighbour.position_y:
                    light.neighbours.append(neighbour)
                if light.position_x == neighbour.position_x + 1 and light.position_y == neighbour.position_y:
                    light.neighbours.append(neighbour)
                if light.position_x == neighbour.position_x and light.position_y == neighbour.position_y + 1:
                    light.neighbours.append(neighbour)
                if light.position_x == neighbour.position_x and light.position_y == neighbour.position_y - 1:
                    light.neighbours.append(neighbour)

    def return_table(self):
        table = []
        for row in range(self.rows):
            rows = []
            for column in range(self.columns):
                for light in self.lights:
                    if light.position_x == row + 1 and light.position_y == column + 1:
                        rows.append(light)
            table.append(rows)
        return table



    def __repr__(self):
        return str(self.lights)