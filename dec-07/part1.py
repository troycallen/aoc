# Read input file
lines = []
with open("dec-07/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

total = 0

# Process each line
for line in lines:
    # Parse target product and numbers
    target_product = int(line.split(":")[0])
    numbers = [int(i) for i in line.split(":")[1].strip().split()]
    print(target_product, numbers)
    
    # Try all possible operation combinations
    num_operations = len(numbers) - 1
    for t in range(2**num_operations):
        # Convert number to binary operations (0 = add, 1 = multiply)
        operations = bin(t)[2:].zfill(num_operations)
        
        # Calculate result using the current operation pattern
        result = numbers[0]
        for i, operation in enumerate(operations):
            if operation == "0":
                result += numbers[i + 1]
            else:
                result *= numbers[i + 1]
        
        # Check if we found the target product
        if result == target_product:
            print(target_product)
            total += target_product
            break

print(total)