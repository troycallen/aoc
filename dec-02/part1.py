with open("dec-02/input.txt", "r") as file:
    sequences = [[int(i) for i in line.split()] for line in file]

safe_count = 0
for levels in sequences:
    incr = levels[1] > levels[0]
    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    if incr:
        safe = all(1 <= diff <= 3 for diff in diffs)
    else:
        safe = all(-3 <= diff <= -1 for diff in diffs)
        
    safe_count += safe

print(safe_count)