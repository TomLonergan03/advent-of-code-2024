with open('../input/day_5.txt') as f:
    input = f.read()

ordering_rules_str, orders_str = input.split('\n\n')

ordering_rules = {}
for rule in ordering_rules_str.split('\n'):
    rule = rule.split('|')
    if int(rule[1]) not in ordering_rules:
        ordering_rules[int(rule[1])] = [int(rule[0])]
    else:
        ordering_rules[int(rule[1])].append(int(rule[0]))

orders = []
for order in orders_str.split('\n'):
    if order:
        orders.append(list(map(int, order.split(','))))

part_1 = 0


def get_relevant_rules(current, order, ordering_rules):
    return list(
        filter(lambda x: x in order, ordering_rules.get(current, [])))


def is_in_order(order, ordering_rules):
    for i in range(0, len(order)):
        rules = get_relevant_rules(order[i], order, ordering_rules)
        for rule in rules:
            if rule not in order[:i]:
                return False
    return True


for order in orders:
    if is_in_order(order, ordering_rules):
        part_1 += order[len(order) // 2]

print("part 1:", part_1)


def fix(order, ordering_rules):
    for i in range(0, len(order)):
        rules = get_relevant_rules(order[i], order, ordering_rules)
        for rule in rules:
            if rule not in order[:i]:
                next = order.index(rule)
                fixed = order[:]
                fixed[next] = order[i]
                fixed[i] = order[next]
                return fixed
    return order


part_2 = 0
swaps = 0
for order in orders:
    if is_in_order(order, ordering_rules):
        continue
    fixed = order[::]
    while not is_in_order(fixed, ordering_rules):
        fixed = fix(fixed, ordering_rules)
        swaps += 1
    part_2 += fixed[len(fixed) // 2]

print("part 2:", part_2, "in", swaps, "swaps")
