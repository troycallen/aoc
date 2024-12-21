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
        
    numbers = [int(i) for i in line.split('|' if getting_rules else ',')]
    if getting_rules:
        rules.append(numbers)
    else:
        updates.append(numbers)

# Build dependency dictionary
dependencies = {}
for rule in rules:
    dependencies.setdefault(rule[0], []).append(rule[1])

# Process updates
for update in updates:
    # Check if order is valid
    valid = True
    for i, current in enumerate(update):
        if current in dependencies:
            if any(update[j] in dependencies[current] for j in range(i)):
                valid = False
                break
    
    # Fix invalid orders
    if not valid:
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if update[j] in dependencies:
                    if update[i] in dependencies[update[j]]:
                        update[i], update[j] = update[j], update[i]
        
        print(update)
        total += update[len(update)//2]

print(total)