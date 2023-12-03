import re
color_max = {'red':12,'blue':14,'green':13}
color_high = {'red':0,'blue':0,'green':0}
pattern = r'([0-9]*) (blue|green|red)'
game_pattern = r'Game ([0-9]*):'

def part_1(input: str) -> int:
    games = []
    total = 0
    
    for line in input.split('\n'):
        impossible = True
        matches = re.finditer(game_pattern, line)
        curr_game = [(match.group(1)) for match in matches]
        for game in line.split('; '):
            matches = re.finditer(pattern, game)
            all_pulls = [[(match.group(1)),(match.group(2))] for match in matches]
            for pull in all_pulls:
                if int(pull[0]) > color_max.get(pull[1]):
                    impossible = False
                    break
            if impossible == False:
                break
        if impossible == True:
            
            total += int(curr_game[0])
    
    return total

def part_2(input: str) -> int:
    total = 0
    for line in input.split('\n'):
        matches = re.finditer(pattern, line)
        all_pulls = [[(match.group(1)),(match.group(2))] for match in matches]
        for pull in all_pulls:
            if int(pull[0]) > color_high.get(pull[1]):
                color_high[pull[1]] = int(pull[0])
        total += (color_high.get('red') * color_high.get('green') * color_high.get('blue'))
        color_high['red'] = 0
        color_high['blue'] = 0
        color_high['green'] = 0
    
    return total

def main():
    with open('day2_input.txt') as f:
        input = f.read()
    
    # Part 1
    part1_total = part_1(input)
    print("Day 2, Part 1's answer is: {sum}".format(sum=part1_total))
    
    part2_total = part_2(input)
    print("Day 2, Part 2's answer is: {sum}".format(sum=part2_total))

if __name__ == "__main__":
    main()