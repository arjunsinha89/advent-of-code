
priorities = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('input.txt') as file:
    lines = file.read().splitlines()

priority = 0
index = 0
length = len(lines)

while index < length:
    first_rucksack = set(lines[index])
    second_rucksack = set(lines[index+1])
    third_rucksack = set(lines[index+2])

    priority += priorities.index(str(first_rucksack.intersection(second_rucksack.intersection(third_rucksack)))[2])
    index += 3

print(priority)
