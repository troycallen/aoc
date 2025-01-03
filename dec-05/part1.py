# Read input file
lines = []
with open("dec-05/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# Parse rules and updates
total = 0
rules = []
updates = []
getting_rules = True

for line in lines:
    if line == "":
        getting_rules = False
        continue
    
    if getting_rules:
        rules.append([int(i) for i in line.split("|")])
    else:
        updates.append([int(i) for i in line.split(",")])

# Build dependency dictionary
dependencies = {}
for rule in rules:
    dependencies.setdefault(rule[0], []).append(rule[1])

# Process updates
for update in updates:
    valid = True
    for i, current in enumerate(update):
        if current in dependencies:
            if any(update[j] in dependencies[current] for j in range(i)):
                valid = False
                break
    
    if valid:
        total += update[len(update) // 2]

print(total)