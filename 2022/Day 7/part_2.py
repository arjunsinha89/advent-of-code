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


TOTAL_DISK_SPACE = 70000000
DISK_SPACE_REQUIRED = 30000000
used_space = sizes['/']
remaining_space = TOTAL_DISK_SPACE - used_space
space_to_delete = DISK_SPACE_REQUIRED - remaining_space


sorted_dict = sorted(sizes.items(), key=lambda x: x[1])
for directory in sorted_dict:
    if directory[1] >= space_to_delete:
        print(directory[1])
        break


