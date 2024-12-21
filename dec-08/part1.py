# Read input file
lines = []
with open("dec-08/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# Initialize variables
total = 0
ant_positions = {}
width = len(lines[0])
height = len(lines)

# Collect ant positions by type
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            ant_positions.setdefault(char, [])
            ant_positions[char].append((x, y))

# Find valid reflected positions
valid_positions = []
for ant_type, positions in ant_positions.items():
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i != j:
                # Calculate reflected position
                x = positions[i][0] * 2 - positions[j][0]
                y = positions[i][1] * 2 - positions[j][1]
                reflected_pos = (x, y)
                
                # Check if position is valid
                if (0 <= x < width and 0 <= y < height and 
                    reflected_pos not in valid_positions):
                    valid_positions.append(reflected_pos)
                    total += 1

print(ant_positions)
print(total)