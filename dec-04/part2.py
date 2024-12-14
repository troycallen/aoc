lines = []
with open("dec-04/input.txt", "r") as file:
    lines = [line.strip() for line in file]

total = 0
height = len(lines)
width = len(lines[0])

# Check each position (excluding edges)
for x in range(1, height - 1):
    for y in range(1, width - 1):
        patterns = ["MAS", "SAM"]
        
        # For each center position, check if it's part of a valid pattern
        for pattern1 in patterns:
            for pattern2 in patterns:
                is_valid = True
                
                for i in range(-1, 2):
                    if lines[x+i][y+i] != pattern1[i+1]:
                        is_valid = False

                for i in range(-1, 2):
                    if lines[x+i][y-i] != pattern2[i+1]:
                        is_valid = False

                if is_valid:
                    total += 1

print(total)