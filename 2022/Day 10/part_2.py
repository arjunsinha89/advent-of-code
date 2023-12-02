
with open('input.txt') as file:
    lines = file.read().splitlines()


registers = []
X = 1
current_pixel = 0

current_row = ''


for line in lines:
    line = line.split(' ')
    if line[0] == 'noop':
        # registers.append(X)
        if(abs(current_pixel - X) < 2):
            current_row += '#'
        else:
            current_row += '.'
        current_pixel += 1
        if current_pixel > 39:
            current_pixel = 0
            print(current_row)
            current_row = ''

        continue
    if line[0] == 'addx':
        
        increment = int(line[1])
        # registers.append(X)
        if(abs(current_pixel - X) < 2):
            current_row += '#'
        else:
            current_row += '.'
        current_pixel += 1
        if current_pixel > 39:
            current_pixel = 0
            print(current_row)
            current_row = ''
        
        
        # registers.append(X)
        if(abs(current_pixel - X) < 2):
            current_row += '#'
        else:
            current_row += '.'
        current_pixel += 1
        if current_pixel > 39:
            current_pixel = 0
            print(current_row)
            current_row = ''
        X += increment

# sum = 0


# for cycle in cycles:
#     sum += (registers[cycle-1]* cycle)
# print(sum)