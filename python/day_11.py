from time import time


def solve():
    def apply_rules(stones: list[int], times: int) -> int:
        seen = {}

        def rec(stone: int, iters_left: int) -> int:
            if (stone, iters_left) in seen:
                return seen[(stone, iters_left)]
            stone_str = str(stone)
            if iters_left == 0:
                return 1
            if stone == 0:
                result = rec(1, iters_left - 1)
                seen[(stone, iters_left)] = result
                return result
            elif len(stone_str) % 2 == 0:
                result = rec(int(stone_str[:len(stone_str) // 2]), iters_left - 1) + rec(
                    int(stone_str[len(stone_str) // 2:]), iters_left - 1)
                seen[(stone, iters_left)] = result
                return result
            else:
                result = rec(stone * 2024, iters_left - 1)
                seen[(stone, iters_left)] = result
                return result

        result = 0
        for stone in stones:
            result += rec(stone, times)
        return result

    with open('../input/day_11.txt') as f:
        input = f.read().replace('\n', '')

    start = time()
    stones = list(map(int, input.split()))
    print("part 1:", apply_rules(stones, 25), "in",
          round(time() - start, 2), "seconds")

    start = time()
    print("part 2:", apply_rules(stones, 75), "in",
          round(time() - start, 2), "seconds")
