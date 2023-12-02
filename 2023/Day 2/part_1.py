
STARTING_POSITIONS = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

sum = 0
with open('input.txt') as file:
    lines = file.read().splitlines()

for line in lines:
    valid = True
    game_id = int(line.split(':')[0].split(' ')[1])
    info = line.split(':')[1].split(';')
    for turn in info:
        for cube in turn.split(','):
            check = cube.split(' ')
            if int(check[1]) > STARTING_POSITIONS[check[2]]:
                valid = False
    if valid:
        sum += game_id
print(sum)
