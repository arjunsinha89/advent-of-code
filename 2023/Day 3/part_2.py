
with open('input.txt') as file:
    lines = file.read().splitlines()

grid = []

symbol_map = {}




for line in lines:
    row = []
    for char in line:
        row.append(char)
    grid.append(row)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '*':
            symbol_map[(i,j)] = []


sum = 0
row_num = 0
for row in grid:
    num = 0
    start_position = -1
    for i in range(0, len(row)):
        if row[i].isdigit():
            if start_position == -1:
                start_position = i
            num = num * 10 + int(row[i])

        if (row[i].isdigit() and i == len(row)-1) or (not row[i].isdigit() and start_position > -1):
            add_num = False
            end_position = i-1
            if start_position > 0 and row[start_position - 1] == '*':
                add_num = True
                symbol_map[(row_num, start_position - 1)].append(num)
                
            elif end_position < len(row)-1 and row[end_position + 1] == '*':
                add_num = True
                symbol_map[(row_num, end_position + 1)].append(num)
                
            else:
                for j in range(start_position-1, end_position+2):
                    if row_num>0:
                        if grid[row_num-1][j]=='*':
                            add_num = True
                            symbol_map[(row_num-1, j)].append(num)
                    
                    if row_num<len(grid)-1:
                        if grid[row_num+1][j]=='*':
                            add_num = True
                            symbol_map[(row_num+1, j)].append(num)
            start_position = -1
            num = 0
    row_num += 1


for k,v in symbol_map.items():
    if len(v) == 2:
        sum += v[0]*v[1]

print(sum)

            
                
            
            


