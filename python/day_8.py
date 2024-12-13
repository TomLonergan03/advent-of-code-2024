from grid import Grid
from itertools import combinations

with open('../input/day_8.txt') as f:
    input = f.readlines()

grid = Grid(input)
signals = set("".join(input).replace('.', '').replace('\n', ''))
towers = [grid.find_matches(signal) for signal in signals]
for signal in towers:
    for (x1, y1), (x2, y2) in combinations(signal, 2):
        dx = x2 - x1
        dy = y2 - y1
        grid.set(x1 - dx, y1 - dy, '#', panic_on_fail=False)
        grid.set(x2 + dx, y2 + dy, '#', panic_on_fail=False)

print("part 1:", grid.count('#'))

grid = Grid(input)
signals = set("".join(input).replace('.', '').replace('\n', ''))
towers = [grid.find_matches(signal) for signal in signals]
for signal in towers:
    for (x1, y1), (x2, y2) in combinations(signal, 2):
        dx = x2 - x1
        dy = y2 - y1
        step = 0
        run = True
        while run:
            set1 = grid.set(x1 - step * dx, y1 - step *
                            dy, '#', panic_on_fail=False)
            set2 = grid.set(x2 + step * dx, y2 + step *
                            dy, '#', panic_on_fail=False)
            run = set1 or set2
            step += 1

print("part 2:", grid.count('#'))
