
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

max_scenic_score = 0

for i in range(num_rows):
    for j in range(num_cols):
        
        
        if i == 0 or j == 0 or i == num_rows - 1 or j == num_cols -1:
            count_visible += 1
            continue 
        is_visible = True
        north_trees = []
        south_trees = []
        west_trees = []
        east_trees = []
        for k in range(i-1,-1,-1):
            north_trees.append(grid[k][j])
            if grid[i][j] <= grid[k][j]:
                is_visible = False
                break
        
        for k in range(i+1, num_rows):
            south_trees.append(grid[k][j])
            if grid[i][j] <= grid[k][j]:
                is_visible = False
                break

        for k in range(j-1,-1,-1):
            west_trees.append(grid[i][k])
            if grid[i][j] <= grid[i][k]:
                is_visible = False
                break
        
        for k in range(j+1, num_cols):
            east_trees.append(grid[i][k])
            if grid[i][j] <= grid[i][k]:
                is_visible = False
                break

        if is_visible:
            count_visible += 1

        else:
            scenic_score = len(north_trees) * len(south_trees) * len(west_trees) * len(east_trees)
            max_scenic_score = max(max_scenic_score, scenic_score)
        
        

print(max_scenic_score)
