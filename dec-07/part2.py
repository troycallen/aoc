# Read input file
lines = []
with open("dec-07/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

total = 0

# Process each line
for line in lines:
    # Parse target product and numbers
    target = int(line.split(":")[0])
    numbers = [int(i) for i in line.split(":")[1].strip().split()]
    print(target, numbers)
    
    # Try all possible operation combinations
    num_operations = len(numbers) - 1
    for t in range(3**num_operations):
        # Convert to base-3 operations (0=add, 1=multiply, 2=concatenate)
        operations = ""
        n = t
        while len(operations) < num_operations:
            operations = str(n % 3) + operations
            n //= 3
        
        # Calculate result using the current operation pattern
        result = numbers[0]
        for i, operation in enumerate(operations):
            if operation == "0":
                result += numbers[i + 1]
            elif operation == "1":
                result *= numbers[i + 1]
            else:  # operation == "2"
                result = int(str(result) + str(numbers[i + 1]))
        
        # Check if we found the target
        if result == target:
            print(target)
            total += target
            break

print(total)