from time import time

from grid import Grid


def replace_region(grid: Grid, x: int, y: int, region_number: int):
    current_region = grid.get(x, y)
    if type(current_region) == int:
        return
    grid.set(x, y, region_number)
    left = grid.get(x - 1, y)
    right = grid.get(x + 1, y)
    up = grid.get(x, y + 1)
    down = grid.get(x, y - 1)
    if left == current_region:
        replace_region(grid, x - 1, y, region_number)
    if right == current_region:
        replace_region(grid, x + 1, y, region_number)
    if up == current_region:
        replace_region(grid, x, y + 1, region_number)
    if down == current_region:
        replace_region(grid, x, y - 1, region_number)


with open('../input/day_12.txt') as f:
    input = f.readlines()

start = time()
grid = Grid(input)
region_number = 0
for x in range(grid.max_x + 1):
    for y in range(grid.max_y + 1):
        region = grid.get(x, y)
        if not region or type(region) == int:
            continue
        replace_region(grid, x, y, region_number)
        region_number += 1

regions = {}
for x in range(grid.max_x + 1):
    for y in range(grid.max_y + 1):
        region = grid.get(x, y)
        if region in regions:
            regions[region][0] += 1
        else:
            regions[region] = [1, 0]
        left = grid.get(x - 1, y)
        right = grid.get(x + 1, y)
        up = grid.get(x, y + 1)
        down = grid.get(x, y - 1)
        reachable = []
        if left == None or left != region:
            regions[region][1] += 1
        if right == None or right != region:
            regions[region][1] += 1
        if up == None or up != region:
            regions[region][1] += 1
        if down == None or down != region:
            regions[region][1] += 1

price = 0
for region, (area, perimeter) in regions.items():
    price += area * perimeter

print("part 1:", price, "in",
      round(time() - start, 2), "seconds")

start = time()
print("part 2:", 0, "in",
      round(time() - start, 2), "seconds")
