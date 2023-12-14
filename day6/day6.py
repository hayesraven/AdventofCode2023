import re

#input = [[7, 9], [15, 40], [30, 200]]                       # Test input
input = [[53, 250], [91, 1330], [67, 1081], [68, 1025]]    # Real input

def part_1(time: int, dist: int) -> int:
    ways_to_win = 0

    for i in range(0, time):
        speed = i
        time_left = time - i
        if speed * time_left > dist:
            ways_to_win += 1

    return ways_to_win

if __name__ == "__main__":

    margin = 1
    for race in input:
        margin *= part_1(race[0], race[1])

    print("Day 6, Part 1's answer is: {margin}".format(margin=margin))

    time = ""
    dist = ""
    for race in input:
        time += str(race[0])
        dist += str(race[1])

    ways_to_win = part_1(int(time), int(dist))

    print("Day 6, Part 2's answer is: {ways_to_win}".format(ways_to_win=ways_to_win))
