import re

def part_1(input: list) -> int:
    lowest = float('inf')

    # Prep input
    data = []
    curr = []
    for i in range(0, len(input)):
        nums = re.findall(r'[0-9]{1,2}', input[i])
        if i == 0:
            data.append(nums)
        elif not re.search(r'[0-9]', input[i]) and len(curr) > 0:
            data.append(curr)
            curr = []
        elif len(nums) > 0:
            curr.append(nums)

    data.append(curr)
    seeds = data.pop(0)

    for seed in seeds:
        s = int(seed)
        for map in data:
            for transform in map:
                if s >= int(transform[1]) and s < int(transform[1]) + int(transform[2]):
                    s = int(transform[0]) + (abs(s - int(transform[1])))
                    break
        if s < lowest:
            lowest = s

    return lowest
    
if __name__ == "__main__":
    with open("day4_input.txt", 'r') as f:
        input = f.read()

    lowest = part_1(input.split('\n')) 
    print("Day 5, Part 1's answer is: {lowest}".format(lowest=lowest))
