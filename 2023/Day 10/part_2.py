with open('input.txt') as file:
    lines = file.readlines()

grid = []
in_loop = []

row = 0

for line in lines:
    line = line.strip('\n')
    grid.append(line)
    loop = []
    for character in line:
        if character == 'S':
            starting_position = [row, line.index('S')]
        loop.append('I')
    in_loop.append(loop)
    row += 1


in_loop[starting_position[0]][starting_position[1]] = 'X'

directions = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1]
}
pipe_done = False
max_distance = -1
for k,v in directions.items():
    current_direction = k
    distance_from_origin = 0
    current_position = [sum(x) for x in zip(starting_position, v)]
    pipe_type = grid[current_position[0]][current_position[1]]
    if k == 'U':
        if pipe_type != 'F' and pipe_type != '7' and pipe_type != '|':
            continue
    
    if k == 'D':
        if pipe_type != 'J' and pipe_type != 'L' and pipe_type != '|':
            continue

    if k == 'L':
        if pipe_type != 'F' and pipe_type != 'L' and pipe_type != '-':
            continue
    
    if k == 'R':
        if pipe_type != 'J' and pipe_type != '7' and pipe_type != '-':
            continue
    
    while pipe_type != '.':
        pipe_done = True
        if current_position[0] < 0 or current_position[0] >= len(grid[0]) or current_position[1] < 0 or current_position[1] >= len(grid[0]):
            break
        in_loop[current_position[0]][current_position[1]] = 'X'

        if pipe_type == 'S':
            break
        

        
        if pipe_type == 'L':
            if current_direction == 'L':
                current_direction = 'U'
            elif current_direction == 'D':
                current_direction = 'R'
        
        if pipe_type == 'J':
            if current_direction == 'R':
                current_direction = 'U'
            elif current_direction == 'D':
                current_direction = 'L'
        
        if pipe_type == '7':
            if current_direction == 'R':
                current_direction = 'D'
            elif current_direction == 'U':
                current_direction = 'L'
        
        if pipe_type == 'F':
            if current_direction == 'U':
                current_direction = 'R'
            elif current_direction == 'L':
                current_direction = 'D'
        
        current_position = [sum(x) for x in zip(current_position, directions[current_direction])]

        pipe_type = grid[current_position[0]][current_position[1]]
    if pipe_done:
        break


for i in range(len(grid)):
    count = 0
    for j in range(len(grid[i])):
        if in_loop[i][j] == 'X':
            if grid[i][j] == '|' or grid[i][j] == 'F' or grid[i][j] == '7' or grid[i][j] == 'S':
                count += 1
        elif count %2 == 0:
            in_loop[i][j] = 'O'
            


count = 0
for row in in_loop:
    for column in row:
        if column == 'I':
            count += 1

print(count)