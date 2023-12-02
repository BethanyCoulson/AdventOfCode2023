import re

with open("input1.txt") as f: #Open file with inputs
    inputs = f.readlines() #Creates a list with each element being a line of inputs

def part1():
    part1_total = 0
    numbers = []
    digits = ["1","2","3","4","5","6","7","8","9"]
    for line in inputs: #Iterates over each string/line
        nums = []
        for character in line: #Iterates over the characters 
            if character in digits: #And compares them to the digits
                nums.append(character) #Adds characters to a list if they are a digit
        numbers.append(int(nums[0] + nums[-1])) #Adds the first and last digit from the line together and add to a list of all the calcualted numbers
    part1_total = sum(numbers) #Adds all the calculated numbers together
    print(part1_total)

def part2():
    part2_total = 0
    digits = {            #Defines a dictionary to convert digits that are written to single character digits
        "one" : "1",
        "two" : "2",
        "three": "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
        "1" : "1",
        "2" : "2",
        "3" : "3",
        "4" : "4",
        "5" : "5",
        "6" : "6",
        "7" : "7",
        "8" : "8",
        "9" : "9",}
    for line in inputs:
        line_digits = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line) #Finds all occurences of digits, uses lookahead assertion to account for overlaps
        num = int(digits[line_digits[0]] + digits[line_digits[-1]]) #Adds first and last occurences of digits together
        part2_total += num #Adds the occurence to the running total for part2
    print(part2_total)

part1()
part2()    
