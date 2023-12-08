with open('input.txt') as file:
    lines = file.readlines()

instructions = lines[0].strip('\n')

# starting_node = lines[2].split(' ')[0]
# ending_node = lines[-1].split(' ')[0]

starting_node = 'AAA'
ending_node = 'ZZZ'

current_node = starting_node


node_map = {}

for line in lines[2:]:
    line = line.replace(' ','').replace('\n','').replace('(','').replace(')','')
    node = line.split('=')[0]
    next_nodes = line.split('=')[1].split(',')
    node_map[node] = next_nodes


step_count = 0
instruction_index = 0

while current_node != ending_node:
    # print(current_node)
    step_count += 1
    instruction = instructions[instruction_index]
    if instruction == 'L':
        current_node = node_map[current_node][0]
    elif instruction == 'R':  
        current_node = node_map[current_node][1]
    instruction_index += 1
    instruction_index %= len(instructions)

print(step_count)