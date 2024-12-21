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

print(obstacles)
print(gx, gy)

# Track visited positions and directions
visited = [(gx, gy)]
visited_with_dirs = [(gx, gy, 0)]
boxes = []
facing = 0

# Define movement directions (up, right, down, left)
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
width = len(lines[0])
height = len(lines)

# First pass: record path
while True:
    # Rotate until valid move found
    while (gx + dirs[facing][0], gy + dirs[facing][1]) in obstacles:
        facing = (facing + 1) % 4
        visited_with_dirs.append((gx, gy, facing))
    
    # Move in current direction
    gx += dirs[facing][0]
    gy += dirs[facing][1]
    
    # Check if out of bounds
    if not (0 <= gx < width and 0 <= gy < height):
        break
    
    visited_with_dirs.append((gx, gy, facing))

# Second pass: find boxes
for index, (px, py, pfacing) in enumerate(visited_with_dirs):
    next_pos = (px + dirs[pfacing][0], py + dirs[pfacing][1])
    
    # Check if potential box position is valid
    if next_pos not in boxes and next_pos not in visited:
        # Temporarily add obstacle to test box completion
        obstacles.append(next_pos)
        
        # Initialize test path
        test_visited = [(px, py, pfacing)]
        gx, gy = px, py
        facing = pfacing
        
        # Try to complete the box
        while True:
            while (gx + dirs[facing][0], gy + dirs[facing][1]) in obstacles:
                test_visited.append((gx, gy, facing))
                facing = (facing + 1) % 4
            
            gx += dirs[facing][0]
            gy += dirs[facing][1]
            
            # Check bounds
            if not (0 <= gx < width and 0 <= gy < height):
                break
                
            current_state = (gx, gy, facing)
            if current_state in test_visited:
                total += 1
                box_pos = (px + dirs[pfacing][0], py + dirs[pfacing][1])
                boxes.append(box_pos)
                print(boxes[-1])
                break
                
            test_visited.append(current_state)
        
        obstacles.pop()
    
    visited.append((px, py))
    if index % 100 == 0:
        print(index)

print(total)