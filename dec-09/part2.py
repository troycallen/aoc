# Read input file
lines = []
with open("dec-09/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# Initialize variables
blocks = []
total = 0

# Generate initial block arrangement
for i, char in enumerate(lines[0]):
    count = int(char)
    if i % 2 == 0:
        blocks.extend([i // 2] * count)
    else:
        blocks.extend([-1] * count)

# Process blocks from right to left
for block_num in range(len(lines[0]) // 2, -1, -1):
    # Get required number of free spaces
    required_spaces = int(lines[0][2 * block_num])
    current_position = blocks.index(block_num)
    
    # Track free space sequences
    free_space_start = None
    current_free_count = 0
    print(block_num)
    
    # Check positions before current block
    for pos in range(current_position):
        if blocks[pos] == -1:
            current_free_count += 1
            # Mark start of free space sequence
            if free_space_start is None:
                free_space_start = pos
                
            # If we have enough free spaces, perform swap
            if current_free_count == required_spaces:
                # Swap blocks
                for i in range(required_spaces):
                    blocks[free_space_start + i], blocks[current_position + i] = \
                        blocks[current_position + i], blocks[free_space_start + i]
                break
        else:
            # Reset free space tracking when non-empty block found
            free_space_start = None
            current_free_count = 0

# Calculate total
total = sum(i * block for i, block in enumerate(blocks) if block != -1)

# Print result
print("".join(str(i) if i != -1 else "." for i in blocks))
print(total)