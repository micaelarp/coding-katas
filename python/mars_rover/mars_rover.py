class MarsRover:
    def __init__(self, x, y, direction, obstacles=None):
        self.x = x
        self.y = y
        self.direction = direction
        self.obstacles = obstacles if obstacles else []

    def execute(self, commands):
        for command in commands:
            if command == "M":
                if self.direction == "N":
                    next_y = (self.y + 1) % 10
                    if [self.x, next_y] in self.obstacles:
                        return f"O:{self.x}:{self.y}:{self.direction}"
                    self.y = next_y
                elif self.direction == "S":
                    next_y = (self.y - 1) % 10
                    if [self.x, next_y] in self.obstacles:
                        return f"O:{self.x}:{self.y}:{self.direction}"
                    self.y = next_y
                elif self.direction == "E":
                    next_x = (self.x + 1) % 10
                    if [next_x, self.y] in self.obstacles:
                        return f"O:{self.x}:{self.y}:{self.direction}"
                    self.x = next_x
                elif self.direction == "W":
                    next_x = (self.x - 1) % 10
                    if [next_x, self.y] in self.obstacles:
                        return f"O:{self.x}:{self.y}:{self.direction}"
                    self.x = next_x
            elif command == "L":
                if self.direction == "N":
                    self.direction = "W"
                elif self.direction == "W":
                    self.direction = "S"
                elif self.direction == "S":
                    self.direction = "E"
                elif self.direction == "E":
                    self.direction = "N"
            elif command == "R":
                if self.direction == "N":
                    self.direction = "E"
                elif self.direction == "E":
                    self.direction = "S"
                elif self.direction == "S":
                    self.direction = "W"
                elif self.direction == "W":
                    self.direction = "N"

        return f"{self.x}:{self.y}:{self.direction}"
