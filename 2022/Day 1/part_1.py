with open('input.txt') as file:
    lines = file.readlines()

largest_calories = 0
current_calories = 0

for line in lines:
    if line == '\n':
        largest_calories = max(current_calories, largest_calories)
        current_calories = 0
    else:
        line = line.strip('\n')
        current_calories += int(line)
    
print(largest_calories)