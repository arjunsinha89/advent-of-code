with open('input.txt') as file:
    lines = file.readlines()

grid = []
starting_position = (-1,-1)

row = 0

for line in lines:
    grid.append(line.strip('\n'))
    if 'S' in line:
        starting_position = [row, line.index('S')]
    row += 1



directions = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1]
}
max_distance = -1
for k,v in directions.items():
    current_direction = k
    distance_from_origin = 0
    current_position = [sum(x) for x in zip(starting_position, v)]
    pipe_type = grid[current_position[0]][current_position[1]]
    while pipe_type != '.':

        distance_from_origin += 1
        if pipe_type == 'S':
            break
        # print(pipe_type)
        # print(current_position)
        if current_position[0] < 0 or current_position[0] >= len(grid) or current_position[1] < 0 or current_position[1] >= len(grid[0]):
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
    max_distance = max((distance_from_origin)/2, max_distance)


# for row in distances:
#     for column in row:
#         if isinstance(column, int):
#             max_distance = max(max_distance,column)
    
print(max_distance)