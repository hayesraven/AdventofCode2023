import re
from enum import Enum

dir_conv = {'L':0, 'R':1}

def parse_nodes(input: list) -> dict:
    nodes = {}

    for item in input:
        
        node = re.search(r'^[a-zA-Z]{3}', item).group(0)
        dirs = re.search(r'\(.*\)', item).group(0)
        nodes[node] = re.findall(r'[a-zA-Z]{3}', dirs)

    return nodes

def part_1(directions: str, nodes: dict) -> int:
    steps = 0
    index = 0

    curr = 'AAA'
    options = nodes.get(curr)
    while True:
        if index == len(directions):
            index = 0
        dir = directions[index]
        curr = options[dir_conv.get(dir)]
        options = nodes.get(curr)
        steps += 1
        index += 1
        if curr == 'ZZZ':
            break

    return steps

if __name__ == "__main__":
    with open("day8_input.txt", 'r') as f:
        input = f.read()

    directions = input.split('\n')[0]
    nodes = parse_nodes(input.split('\n')[2:])
    steps = part_1(directions, nodes)
    print("Day 8, Part 1's answer is: {steps}".format(steps=steps))
