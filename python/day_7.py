from time import time


def solve():
    class Equation:
        def __init__(self, s: str):
            self.result = int(s.split(':')[0])
            self.values = list(map(int, s.split(':')[1].strip().split()))

        def can_solve_pt1(self) -> bool:
            def solve(current, operator, values):
                if not values:
                    return current == self.result
                if operator == "*":
                    current *= values[0]
                    if solve(current, "*", values[1:]):
                        return True
                    return solve(current, "+", values[1:])
                else:
                    current += values[0]
                    if solve(current, "*", values[1:]):
                        return True
                    return solve(current, "+", values[1:])
            return solve(0, "+", self.values)

        def can_solve_pt2(self) -> bool:
            def solve(current, operator, values):
                if not values:
                    return current == self.result
                if operator == "*":
                    current *= values[0]
                    if solve(current, "*", values[1:]):
                        return True
                    if solve(current, "|", values[1:]):
                        return True
                    return solve(current, "+", values[1:])
                elif operator == "|":
                    current = int(str(current) + str(values[0]))
                    if solve(current, "*", values[1:]):
                        return True
                    if solve(current, "|", values[1:]):
                        return True
                    return solve(current, "+", values[1:])
                else:
                    current += values[0]
                    if solve(current, "*", values[1:]):
                        return True
                    if solve(current, "|", values[1:]):
                        return True
                    return solve(current, "+", values[1:])

            return solve(0, "+", self.values)

    with open('../input/day_7.txt') as f:
        input = f.readlines()

    start = time()
    equations = map(lambda x: Equation(x), input)
    part_1 = sum(map(lambda x: x.result, filter(
        lambda x: x.can_solve_pt1(), equations)))
    print("part 1:", part_1, "in", round(time() - start, 2), "s")

    start = time()
    equations = map(lambda x: Equation(x), input)
    part_2 = sum(map(lambda x: x.result, filter(
        lambda x: x.can_solve_pt2(), equations)))
    print("part 2:", part_2, "in", round(time() - start, 2), "s")
