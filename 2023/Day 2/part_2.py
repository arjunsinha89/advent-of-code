

sum = 0
with open('input.txt') as file:
    lines = file.read().splitlines()

for line in lines:

    MIN_CUBES = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    valid = True
    game_id = int(line.split(':')[0].split(' ')[1])
    info = line.split(':')[1].split(';')
    for turn in info:
        for cube in turn.split(','):
            check = cube.split(' ')
            if int(check[1]) > MIN_CUBES[check[2]]:
                MIN_CUBES[check[2]] = int(check[1])
    power = 1
    for color in MIN_CUBES.keys():
        power *= MIN_CUBES[color]
    sum += power
print(sum)
