
priorities = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('input.txt') as file:
    lines = file.read().splitlines()

priority = 0
for line in lines:
    length = len(line)
    l = int(length/2)
    first_half = set(line[:l])
    second_half = set(line[-l:])
    priority += priorities.index(str(first_half.intersection(second_half))[2])
print(priority)
