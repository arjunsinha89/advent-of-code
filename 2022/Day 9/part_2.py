
def move_end(inital_position, move):
    return tuple(map(sum, zip(inital_position, move))) 



POSITION_CHANGE = {
    'U' : (1, 0),
    'D' : (-1, 0),
    'R' : (0, 1),
    'L' : (0, -1)
}

TAIL_POSITIONS = {(0,0)}
NUM_KNOTS = 10

knot_positions = [(0,0)] * NUM_KNOTS

with open('input.txt') as file:
    lines = file.read().splitlines()

for line in lines:
    line = line.split(' ')
    direction = line[0]
    num_moves = int(line[1])
    for i in range(num_moves):
        
        knot_positions[0] = move_end(knot_positions[0], POSITION_CHANGE[direction])
        for j in range(1,len(knot_positions)):
            
            x_distance = knot_positions[j-1][0] - knot_positions[j][0]
            y_distance = knot_positions[j-1][1] - knot_positions[j][1]
            if abs(x_distance) > 1:
                if abs(y_distance) == 0:
                    knot_positions[j] = move_end(knot_positions[j], ((int(abs(x_distance)/x_distance),0)))
                else:
                    knot_positions[j] = move_end(knot_positions[j], ((int(abs(x_distance)/x_distance),(int(abs(y_distance)/y_distance)))))
            elif abs(y_distance) > 1:
                if abs(x_distance) == 0:
                    knot_positions[j] = move_end(knot_positions[j], (0,(int(abs(y_distance)/y_distance))))
                else:
                    knot_positions[j] = move_end(knot_positions[j], ((int(abs(x_distance)/x_distance),(int(abs(y_distance)/y_distance)))))
        
        TAIL_POSITIONS.add(knot_positions[-1])
print(len(TAIL_POSITIONS))
