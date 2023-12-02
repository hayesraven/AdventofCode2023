import re

digit_dict = {
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9',
    "zero":'0'
    }

pattern = r'(?=((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(zero)|([0-9])))'

def part_2(input: str) -> str:
    nums = []
    matches = re.finditer(pattern, input)
    results = [(match.group(1)) for match in matches]
    
    first = digit_dict.get(results[0])
    if first != None:
        nums.append(first)
    else:
        nums.append(results[0])
        
    last = digit_dict.get(results[-1])
    if last != None:
        nums.append(last)
    else:
        nums.append(results[-1])
    
    return int(nums[0] + nums[-1])
    
def part_1(input: str) -> str:  
    nums = []
    for letter in input:
        if ord(letter) <= 57:
            nums.append(letter)
    
    return int(nums[0] + nums[-1])
    
def main():
    with open('day1_input.txt', 'r') as f:
        input = f.read()
    
    # Part 1
    sum = 0
    for line in input.split('\n'):
        sum += part_1(line)
    
    print("Day 1, Part 1's answer is:\n{sum}".format(sum=sum))
    
    with open('day1_input.txt', 'r') as f:
        input = f.read()
        
    # Part 2
    sum = 0
    for line in input.split('\n'):
        sum += part_2(line)

    print("Day 1, Part 2's answer is:\n{sum}".format(sum=sum))

if __name__ == "__main__":
    main()