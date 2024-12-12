# Read file
with open("dec-03/input.txt", "r") as file:
    lines = [line.strip() for line in file]

total = 0
enabled = True

for line in lines:
    # Process each potential starting position
    for i in range(len(line) - 4):  # -4 to ensure room for shortest command
        # Check for mul(
        if line[i:i+4] == "mul(":
            window = line[i+4:i+12]  # Look ahead up to 8 chars for closing )
            for j in range(len(window)):
                if window[j] == ")":
                    nums_str = window[:j]
                    try:
                        nums = [int(x) for x in nums_str.split(",")]
                        if len(nums) == 2 and enabled:
                            if nums[0] < 1000 and nums[1] < 1000:
                                total += nums[0] * nums[1]
                    except Exception:
                        break
                    break

        # Check enable/disable commands
        if line[i:i+4] == "do()":
            enabled = True
        if line[i:i+7] == "don't()":
            enabled = False

print(total)