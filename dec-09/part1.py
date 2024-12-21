# Read input file
lines = []
with open("dec-09/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# Initialize variables
blocks = []
total = 0

# Generate blocks array
for i, char in enumerate(lines[0]):
    count = int(char)
    if i % 2 == 0:
        blocks.extend([i // 2] * count)  # Add numbered blocks
    else:
        blocks.extend([-1] * count)      # Add empty spaces

# Swap blocks from end to beginning
swap_index = -1
for current in range(len(blocks)):
    if blocks[current] == -1:
        # Find next non-empty block from the end
        while blocks[swap_index] == -1:
            swap_index -= 1
            
        # Stop if we've run out of blocks to swap
        if len(blocks) + swap_index <= current:
            break
            
        # Perform the swap
        blocks[swap_index], blocks[current] = blocks[current], blocks[swap_index]

# Calculate total
total = sum(i * block for i, block in enumerate(blocks) if block != -1)

# Print result
print("".join(str(i) if i != -1 else "." for i in blocks))
print(total)