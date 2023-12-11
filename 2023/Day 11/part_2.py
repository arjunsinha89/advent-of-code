with open('input.txt') as file:
    lines = file.readlines()


galaxies = []

rows_to_duplicate = []
columns_to_duplicate = [i for i in range(len(lines[0]))]


EXPANSION_FACTOR = 1000000-1

for i in range(len(lines)):
    if '#' not in lines[i]:
        rows_to_duplicate.append(i)
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            galaxies.append((i, j))
            if j in columns_to_duplicate:
                columns_to_duplicate.remove(j)


for i in range(len(galaxies)):
    galaxies[i] = (galaxies[i][0]+EXPANSION_FACTOR*len([x for x in rows_to_duplicate if x<galaxies[i][0]]), galaxies[i][1]+EXPANSION_FACTOR*len([x for x in columns_to_duplicate if x<galaxies[i][1]]))



sum_path = 0

for galaxy_1 in galaxies:
    for galaxy_2 in galaxies:
        path = abs(galaxy_1[0]-galaxy_2[0])+abs(galaxy_1[1]-galaxy_2[1])
        sum_path += path

print(sum_path/2)

