
def find_first_digit(line):
    for char in line:
        if char.isdigit():
            return int(char)
        
    return -1


lines = []
with open('input.txt') as file:
    lines = file.readlines()

total_sum = 0

for line in lines:
    total_sum += find_first_digit(line)*10 + find_first_digit(line[::-1])
print(total_sum)