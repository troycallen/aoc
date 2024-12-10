from collections import Counter

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
similarity = 0

count2 = Counter(second)
#print(count2)

for i in range(len(first)):
    if first[i] in count2:
        similarity += int(first[i]) * int(count2[first[i]])

print(similarity)