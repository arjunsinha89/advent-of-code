with open('input.txt') as file:
    lines = file.readlines()

times = []
distances = []

for elem in lines[0].strip('\n').split(' '):
    if elem.isdigit():
        times.append(int(elem))


for elem in lines[1].strip('\n').split(' '):
    if elem.isdigit():
        distances.append(int(elem))


total = 1

for i in range(len(times)):
    time = times[i]
    record_distance = distances[i]
    count = 0
    for j in range(time+1):
        distance = j*(time-j)
        if distance > record_distance:
            count += 1
    total = total * count

print(total)

