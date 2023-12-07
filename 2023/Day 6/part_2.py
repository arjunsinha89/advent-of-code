import math
with open('input.txt') as file:
    lines = file.readlines()

time = 0
record_distance = 0

for elem in lines[0].strip('\n'):
    if elem.isdigit():
        time = time*10 + int(elem)

for elem in lines[1].strip('\n'):
    if elem.isdigit():
        record_distance = record_distance*10 + int(elem)

sol_1 = ((time+math.sqrt(time*time - 4*record_distance))/2)
sol_2 = ((time-math.sqrt(time*time - 4*record_distance))/2)


min_range = max(math.ceil(min(sol_1, sol_2)),0)
max_range = min(math.ceil(max(sol_1, sol_2)),time)

print(max_range - min_range)
                
