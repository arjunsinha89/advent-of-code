with open('input.txt') as file:
    lines = file.read().splitlines()

count = 0

for line in lines:
    sections = line.split(',')
    print(sections)
    section_1 = sections[0].split('-')
    section_2 = sections[1].split('-')

    if ((int(section_1[0]) <= int(section_2[1]) and int(section_1[1]) >= int(section_2[0])) 
        or int(section_1[0]) >= int(section_2[1]) and int(section_1[1]) <= int(section_2[0])):
        count += 1

print(count)