def contains_duplicates(buffer):
    length = len(buffer)
    for i in range(0,length):
        for j in range(i+1,length):
            if buffer[i] == buffer[j]:
                return True

    return False


def find_marker(line, buffer_size):


    for i in range(buffer_size-1,len(line)):
        buffer = line[i-buffer_size+1:i+1]
        if contains_duplicates(buffer):
            continue
        return i+1
    return -1

with open('input.txt') as file:
    lines = file.read().splitlines()

line = lines[0]

NUM_CHARACTERS = 14
print(find_marker(line, NUM_CHARACTERS))
    
    