
with open('input.txt') as file:
    lines = file.read().splitlines()

num_rows = len(lines)
num_cols = len(lines[0])
total_trees = num_rows * num_cols

grid = []

for line in lines:
    sequence = []
    for char in line:
        sequence.append(int(char))
    grid.append(sequence)

count_visible = 0

for i in range(num_rows):
    for j in range(num_cols):
        

        if i == 0 or j == 0 or i == num_rows - 1 or j == num_cols -1:
            count_visible += 1
            continue 

        north_trees = []
        south_trees = []
        west_trees = []
        east_trees = []
        for k in range(i):
            north_trees.append(grid[k][j])
        
        for k in range(i+1, num_rows):
            south_trees.append(grid[k][j])

        for k in range(j):
            west_trees.append(grid[i][k])
        
        for k in range(j+1, num_cols):
            east_trees.append(grid[i][k])



        if grid[i][j] > max(north_trees) or grid[i][j] > max(south_trees) or grid[i][j] > max(west_trees) or grid[i][j] > max(east_trees):
            count_visible += 1
        
        

print(count_visible)
