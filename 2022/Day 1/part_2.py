with open('input.txt') as file:
    lines = file.readlines()

elves_calories = []
current_calories = 0

for line in lines:
    if line == '\n':
        elves_calories.append(current_calories)
        current_calories = 0
    else:
        line = line.strip('\n')
        current_calories += int(line)
if current_calories != 0:
    elves_calories.append(current_calories)
    
elves_calories.sort()

print(sum(elves_calories[-3:]))