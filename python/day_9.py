from time import time


def make_blocks(s):
    blocks = {}
    file_no = 0
    block_no = 0
    for i in range(0, len(s), 2):
        for _ in range(int(s[i])):
            blocks[block_no] = file_no
            block_no += 1
        block_no += int(s[i + 1])
        file_no += 1
    return blocks


def compact(blocks):
    def find_next_empty(block_no):
        for i in range(block_no, len(blocks)):
            if i not in blocks:
                return i
        return None

    block_no = max(blocks.keys())
    empty_block = 0
    for current_block_addr in reversed(range(block_no + 1)):
        empty_block = find_next_empty(empty_block)
        if not empty_block or empty_block > current_block_addr:
            break
        if current_block_addr in blocks:
            blocks[empty_block] = blocks[current_block_addr]
            del blocks[current_block_addr]


def compact_files(blocks):
    def find_first_fit(size):
        max_block = max(blocks.keys()) + 1
        for i in range(max_block):
            if i in blocks:
                continue
            if all(map(lambda x: x not in blocks, range(i, i + size))):
                return i
        return None

    sizes = {}
    for k in blocks.keys():
        file = blocks[k]
        if file in sizes:
            sizes[file] += 1
        else:
            sizes[file] = 1

    block_no = max(blocks.keys())
    first_block = block_no
    for current_block_addr in reversed(range(block_no + 1)):
        if current_block_addr % 10000 == 0:
            print(round((first_block - current_block_addr) /
                  first_block * 100, 2), "%", end="\r")
        empty_block = find_first_fit(sizes[blocks.get(current_block_addr, 0)])
        if not empty_block or empty_block > current_block_addr:
            continue
        if current_block_addr in blocks:
            for i in range(sizes[blocks[current_block_addr]]):
                blocks[empty_block + i] = blocks[current_block_addr - i]
                del blocks[current_block_addr - i]


def checksum(blocks):
    total = 0
    for k, v in blocks.items():
        total += k * v
    return total


def print_disk(blocks):
    for i in range(max(blocks.keys()) + 1):
        print(blocks.get(i, "."), end="")
    print()


with open('../input/day_9.txt') as f:
    input = f.read().strip() + "0"

start = time()
blocks = make_blocks(input)
compact(blocks)
print("part 1:", checksum(blocks), "in", round(time() - start, 2), "seconds")

start = time()
blocks = make_blocks(input)
compact_files(blocks)
print("part 2:", checksum(blocks), "in", round(time() - start, 2), "seconds")
