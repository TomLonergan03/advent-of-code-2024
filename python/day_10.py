from time import time
from grid import Grid


def solve():
    def countPaths(grid, x, y) -> list[tuple[int, int]]:
        height = grid.get(x, y)
        if height == None:
            return []
        if height == 9:
            return [(x, y)]
        left = grid.get(x - 1, y)
        right = grid.get(x + 1, y)
        up = grid.get(x, y + 1)
        down = grid.get(x, y - 1)
        reachable = []
        if left and left == height + 1:
            reachable.extend(countPaths(grid, x - 1, y))
        if right and right == height + 1:
            reachable.extend(countPaths(grid, x + 1, y))
        if up and up == height + 1:
            reachable.extend(countPaths(grid, x, y + 1))
        if down and down == height + 1:
            reachable.extend(countPaths(grid, x, y - 1))
        return reachable

    with open('../input/day_10.txt') as f:
        input = f.readlines()

    start = time()
    grid = Grid(input, cast=int)
    possible_starts = grid.find_matches(0)

    trailheads_routes = list(map(lambda loc: countPaths(
        grid, loc[0], loc[1]), possible_starts))

    trailheads_score = sum(map(lambda x: len(set(x)), trailheads_routes))

    print("part 1:", trailheads_score, "in",
          round(time() - start, 2), "seconds")

    start = time()
    trailheads_rating = sum(map(len, trailheads_routes))
    print("part 2:", trailheads_rating, "in",
          round(time() - start, 2), "seconds")
