# Read input file
lines = []
with open("dec-06/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# Initialize variables
total = 0
obstacles = []
gx = gy = 0

# Find starting position and obstacles
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            obstacles.append((x, y))
        if c == "^":
            gx, gy = x, y

# Define movement directions (up, right, down, left)
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
facing = 0  # Start facing up
visited = []

# Navigate maze
width = len(lines[0])
height = len(lines)

while True:
    # Rotate until valid move found
    while (gx + dirs[facing][0], gy + dirs[facing][1]) in obstacles:
        facing = (facing + 1) % 4
    
    # Move in current direction
    gx += dirs[facing][0]
    gy += dirs[facing][1]
    
    # Check if out of bounds
    if not (0 <= gx < width and 0 <= gy < height):
        break
        
    # Track visited positions
    if (gx, gy) not in visited:
        visited.append((gx, gy))
        total += 1
        
print(total)