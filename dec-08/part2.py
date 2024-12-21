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

# Find valid positions along slopes
valid_positions = []
for positions in ant_positions.values():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            pos1 = positions[i]
            pos2 = positions[j]
            
            # Skip if same x-coordinate (vertical line)
            if pos1[0] == pos2[0]:
                continue
                
            # Calculate slope between points
            slope = (pos1[1] - pos2[1]) / (pos1[0] - pos2[0])
            
            # Test positions along the slope
            for step in range(-50, 50):
                y_step = round(slope * step, 8)
                
                # Check if y-step is an integer
                if int(y_step) == y_step:
                    new_pos = (pos1[0] + step, pos1[1] + y_step)
                    
                    # Check if position is valid and new
                    if (0 <= new_pos[0] < width and 
                        0 <= new_pos[1] < height and 
                        new_pos not in valid_positions):
                        valid_positions.append(new_pos)
                        total += 1

print(ant_positions)
print(total)