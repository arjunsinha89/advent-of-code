
with open('input.txt') as file:
    lines = file.read().splitlines()


registers = []
X = 1
cycles = [20, 60, 100, 140, 180, 220]

for line in lines:
    line = line.split(' ')
    if line[0] == 'noop':
        registers.append(X)
        continue
    if line[0] == 'addx':
        increment = int(line[1])
        registers.append(X)
        registers.append(X)
        X += increment

sum = 0


for cycle in cycles:
    sum += (registers[cycle-1]* cycle)
print(sum)