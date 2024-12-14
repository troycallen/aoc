lines = []
with open("dec-04/input.txt", "r") as file:
    lines = [line.strip() for line in file]

total = 0

# Check horizontal patterns
for line in lines:
    total += line.count("XMAS") + line.count("SAMX")

# Check vertical patterns by creating vertical strings
vertical = [''.join(col) for col in zip(*lines)]
for line in vertical:
    total += line.count("XMAS") + line.count("SAMX")

height = len(lines)
width = len(lines[0])
patterns = ["XMAS", "SAMX"]

# Check all possible starting positions
for x in range(height):
    for y in range(width):
        for pattern in patterns:
            try:
                if all(lines[x + i][y + i] == pattern[i] for i in range(4)):
                    total += 1
            except IndexError:
                pass

            try:
                if y >= 3 and all(lines[x + i][y - i] == pattern[i] for i in range(4)):
                    total += 1
            except IndexError:
                pass

print(total)