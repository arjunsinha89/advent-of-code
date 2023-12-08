from math import lcm
with open('input.txt') as file:
    lines = file.readlines()

instructions = lines[0].strip('\n')

# starting_node = lines[2].split(' ')[0]
# ending_node = lines[-1].split(' ')[0]

starting_nodes = []
ending_nodes = []

step_counts = []


node_map = {}

for line in lines[2:]:
    line = line.replace(' ','').replace('\n','').replace('(','').replace(')','')
    node = line.split('=')[0]
    if node[-1] == 'A':
        starting_nodes.append(node)
    if node[-1] == 'Z':
        ending_nodes.append(node)
    next_nodes = line.split('=')[1].split(',')
    node_map[node] = next_nodes


for node in starting_nodes:
    step_count = 0
    current_node = node
    instruction_index = 0

    while current_node not in ending_nodes:
        # print(current_node)
        step_count += 1
        instruction = instructions[instruction_index]
        if instruction == 'L':
            current_node = node_map[current_node][0]
        elif instruction == 'R':  
            current_node = node_map[current_node][1]
        instruction_index += 1
        instruction_index %= len(instructions)

    step_counts.append(step_count)
print(lcm(*step_counts))