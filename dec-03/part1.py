import re

# Read file
with open("dec-03/input.txt", "r") as file:
    lines = [line.strip() for line in file]

# Find and sum all valid multiplications
pattern = r"mul\((\d+),(\d+)\)"
total = 0

for line in lines:
    matches = re.findall(pattern, line)
    for x, y in matches:
        x, y = int(x), int(y)
        if x < 1000 and y < 1000:
            total += x * y

print(total)