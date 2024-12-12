def is_safe_sequence(levels):
    if len(levels) < 2:
        return False
    
    incr = levels[1] > levels[0]
    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    if incr:
        return all(1 <= diff <= 3 for diff in diffs)
    else:
        return all(-3 <= diff <= -1 for diff in diffs)

# Read all sequences
with open("dec-02/input.txt", "r") as file:
    sequences = [[int(i) for i in line.split()] for line in file]

safe_count = 0
for levels in sequences:
    # Check original sequence
    if is_safe_sequence(levels):
        safe_count += 1
        continue
    
    # Try removing one number at a time until a safe sequence is found
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe_sequence(modified_levels):
            safe_count += 1
            break

print(safe_count)