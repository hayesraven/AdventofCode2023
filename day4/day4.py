import re, math

win_pattern = r'\s(([0-9]{1,2}\s+)+)\|'
match_pattern = r'\|\s+(([0-9]{1,2}\s*)+)'

def score_card(card: str) -> int:
    curr = 0
    matches = re.finditer(win_pattern, card)
    curr_win = [(match.group(1)) for match in matches]
    matches = re.finditer(match_pattern, card)
    curr_match = [(match.group(1)) for match in matches]
    curr_win = curr_win[0].split()
    curr_match = curr_match[0].split()
    for win in curr_win:
        if win in curr_match:
            if curr == 0:
                    curr = 1
            else:
                curr *= 2
    
    return curr
    
def part_2(input: list) -> int:
    total = 0
    
    for i in range(0, len(input)):
        cards = 0
        won = score_card(input[i])
        if won != 0:
            cards = int(math.log(won,2) + 1)
            total += 1
            for j in range(i + 1, i + cards + 1):
                total += part_2(input[j:])
        
    return total

def part_1(input: list) -> int:
    total = 0
    
    for card in input:
        total += score_card(card)
    
    return total

def main():
    with open("test_input1.txt", 'r') as f:
        input = f.read()
    
    sum = part_1(input.split('\n'))
    print("Day 4, Part 1's answer is: {sum}".format(sum=sum))
    
    sum = part_2(input.split('\n'))
    print("Day 4, Part 2's answer is: {sum}".format(sum=sum))

if __name__ == "__main__":
    main()