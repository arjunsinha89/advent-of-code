from collections import defaultdict

with open('input.txt') as file:
    lines = file.read().splitlines()


path = []

sizes = defaultdict(int)



for line in lines:
    line = line.split(' ')
    if line[1] == 'cd':
        if line[2] == '..':
            path.pop()
        else:
            path.append(line[2])
    if line[0].isnumeric():
        for i in range(len(path)):
            sizes['/'.join(path[0:i+1])] += int(line[0])


sum = 0
for size in sizes.keys():
    if sizes[size] <= 100000:
        sum += sizes[size]

print(sum)

