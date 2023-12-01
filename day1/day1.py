with open("input1.txt") as f:
    inputs = f.readlines()

def part1():
    part1_total = 0
    numbers = []
    digits = ["1","2","3","4","5","6","7","8","9"]
    for line in inputs:
        nums = []
        for character in line:
            if character in digits:
                nums.append(character)
        numbers.append(int(nums[0] + nums[-1]))
    part1_total = sum(numbers)
    print(part1_total)

part1()    
