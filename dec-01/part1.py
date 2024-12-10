data = []

with open("dec-01/input.txt", "r") as file:
    for line in file:
        data.append(line.strip().split()) 

list1 = []
list2 = []

first = [pair[0] for pair in data]
second = [pair[1] for pair in data]


first.sort()
second.sort()
res = 0

for i in range(len(first)):
    distances = abs(int(first[i]) - int(second[i]))
    res += distances

print(res)