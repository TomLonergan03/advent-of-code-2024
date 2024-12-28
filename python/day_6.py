from grid import Grid
from time import time


def solve():
    def march_guard(grid: Grid, guard: tuple[int, int]) -> tuple[Grid, bool]:
        visited = {}
        terminates = False
        direction = "up"
        while True:
            grid.set(*guard, 'X')
            # if we have visited this location in this direction before, we have a loop
            if guard in visited and direction in visited[guard]:
                break
            elif guard in visited:
                visited[guard].append(direction)
            else:
                visited[guard] = [direction]
            next_move = grid.get_move(*guard, direction)
            if next_move is None:
                terminates = True
                break
            if next_move == '#':
                match direction:
                    case "up":
                        direction = "right"
                    case "right":
                        direction = "down"
                    case "down":
                        direction = "left"
                    case "left":
                        direction = "up"
            else:
                match direction:
                    case "up":
                        guard = (guard[0], guard[1] + 1)
                    case "right":
                        guard = (guard[0] + 1, guard[1])
                    case "down":
                        guard = (guard[0], guard[1] - 1)
                    case "left":
                        guard = (guard[0] - 1, guard[1])
        return (grid, terminates)

    with open('../input/day_6.txt') as f:
        input = f.readlines()

    grid = Grid(input)
    guard = grid.find_matches('^')[0]
    marked_grid, _ = march_guard(grid, guard)
    visited_locations = marked_grid.find_matches('X')
    print("part 1:", len(visited_locations))

    visited_locations = list(filter(lambda x: x != guard, visited_locations))
    locations = 0
    start = time()
    for i in range(len(visited_locations)):
        grid = Grid(input)
        grid.set(*visited_locations[i], '#')
        _, terminates = march_guard(grid, guard)
        if not terminates:
            locations += 1

    print("part 2:", locations)
