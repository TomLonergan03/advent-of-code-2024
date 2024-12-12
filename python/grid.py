from typing import List


class Grid:
    def __init__(self, string: List[str]):
        self.grid = list(map(lambda x: list(x)[:-1], string))
        self.max_y = len(self.grid) - 1
        self.max_x = len(self.grid[0]) - 1

    def get(self, x, y):
        if x < 0 or x > self.max_x or self.max_y - y < 0 or self.max_y - y > self.max_y:
            return None
        return self.grid[self.max_y - y][x]

    def get_str(self):
        return ''.join([''.join(row) for row in self.grid])

    def set(self, x, y, value):
        if x < 0 or x > self.max_x or self.max_y - y < 0 or self.max_y - y > self.max_y:
            raise Exception("out of bounds", (x, y),
                            "maxes are", (self.max_x, self.max_y))
        self.grid[self.max_y - y][x] = value

    def get_move(self, x, y, direction):
        match direction:
            case "up":
                return self.get(x, y + 1)
            case "right":
                return self.get(x + 1, y)
            case "down":
                return self.get(x, y - 1)
            case "left":
                return self.get(x - 1, y)
            case _:
                return None

    def find_matches(self, value) -> List[tuple[int, int]]:
        matches = []
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                if self.get(x, y) == value:
                    matches.append((x, y))
        return matches

    def print(self):
        for row in self.grid:
            print(row)
        print()
