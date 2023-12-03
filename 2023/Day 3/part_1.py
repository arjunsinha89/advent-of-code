
with open('input.txt') as file:
    lines = file.read().splitlines()

grid = []


for line in lines:
    row = []
    for char in line:
        row.append(char)
    grid.append(row)

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
            if start_position > 0 and not (row[start_position - 1] == '.' or row[start_position - 1].isdigit()):
                add_num = True
            elif end_position < len(row)-1 and not (row[end_position + 1] == '.' or row[end_position + 1].isdigit()):
                add_num = True
            else:
                for j in range(start_position-1, end_position+2):
                    if row_num>0:
                        if not (grid[row_num-1][j]=='.' or grid[row_num-1][j].isdigit()):
                            add_num = True
                            break
                    
                    if row_num<len(grid)-1:
                        if not (grid[row_num+1][j]=='.' or grid[row_num+1][j].isdigit()):
                            add_num = True
                            break
            
            # print(start_position)
            # print(end_position)
            if add_num:

                # print(num)
                sum += num
            start_position = -1
            num = 0
    row_num += 1

print(sum)

            
                
            
            


