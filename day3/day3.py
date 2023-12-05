
def check_part(input: list, part_start: int, part_end: int, row: int) -> bool:
    spots_check = []
    
    hori_start = 0
    if part_start != 0:
        hori_start = part_start - 1
        
    hori_end = len(input[row])
    if part_end != len(input[row]):
        hori_end = part_end + 1
    
    if row != 0:
        for i in range(hori_start, hori_end):
            spots_check.append(input[row - 1][i])
            
    for i in range(hori_start, hori_end):
            spots_check.append(input[row][i])
            
    if row != len(input) - 1:
        for i in range(hori_start, hori_end):
            spots_check.append(input[row + 1][i])
            
    for spot in spots_check:
        if not spot.isdigit() and spot != '.':
            return True
    
def part_1(input: list) -> int:
    total = 0
    
    for i in range(0, len(input)):
        j = 0
        in_part = False
        part_start = 0
        while j < len(input[i]):
            if input[i][j].isdigit():
                part_start = j
                while j < len(input[i]) and input[i][j].isdigit():
                    j += 1
                part_end = j
                if check_part(input, part_start, part_end, i):
                    part_num = int(input[i][part_start:part_end])
                    total += part_num
            j += 1
    
    return total

def part_2(input: list) -> int:
    for i in range(0, len(input)):
        j = 0
        while j < len(input[i]):
            if input[i][j] == '*':
                check = []
                if i != 0:
                    check.append(input[i - 1])
                check.append(input[i])
                if i < len(input) - 1:
                    check.append(input[i + 1])
        # To Do

def main():
    with open("day3_input.txt", 'r') as f:
        input = f.read()
        
    sum = part_1(input.split('\n'))    
    print("Day 3, Part 1's answer is {sum}".format(sum=sum))
    

if __name__ == "__main__":
    main()