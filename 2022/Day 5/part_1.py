with open('input.txt') as file:
    lines = file.read().splitlines()

length = len(lines[0])
num_crates = int((length+1)/4)
piles = [''] * num_crates

setup_complete = False

for line in lines:
    if setup_complete:
        if line == '':
            continue
        else:
            line = line.split(' ')
            num_crates = int(line[1])
            origin = int(line[3])
            destination = int(line[5])
            moved_crates = piles[origin-1][-num_crates:]
            piles[origin-1] = piles[origin-1][:-num_crates]
            moved_crates = moved_crates[::-1]
            piles[destination-1] += moved_crates
    else:

        if line[1] == '1':
            setup_complete = True
            continue
        index = 1
        while index < length:
            crate = line[index]

            if crate != ' ':
                piles[int((index-1)/4)] = crate + piles[int((index-1)/4)] 
            index += 4

output = ''
for pile in piles:
    output += pile[-1]

print(output)