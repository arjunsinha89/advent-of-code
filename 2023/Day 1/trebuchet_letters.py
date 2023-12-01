


digit_nums = '123456789'
digit_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

digits = {}

for num, name in zip(digit_nums, digit_names):
    digits[num] = name



def find_first_digit(line):

    for i in range(len(line)):
        for num in digits.keys():
            if num in line[0:i]or digits[num] in line[0:i]:
                return int(num)
    return -1

def find_last_digit(line):
    for i in range(len(line)):
        for num in digits.keys():
            if num in line[-i-1:]or digits[num] in line[-i-1:]:
                return int(num)
    return -1


lines = []
with open('input.txt') as file:
    lines = file.readlines()

total_sum = 0

digit_nums = '123456789'
digit_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

digits = {}

for num, name in zip(digit_nums, digit_names):
    digits[num] = name



for line in lines:
    new_line = line
    total_sum += find_first_digit(line)*10 + find_last_digit(line)
print(total_sum)