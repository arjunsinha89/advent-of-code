with open('input.txt') as file:
    lines = file.readlines()

def is_all_zeros(nums):
    for num in nums:
        if num != 0:
            return False
    return True


total = 0
num_lists = []
for line in lines:
    nums = []
    line = line.strip('\n').split(' ')
    for num in line:
        nums.append(int(num))
    
    check_nums = nums
    num_lists.append(nums[-1])
    while not is_all_zeros(check_nums):
        check_nums = []
        for i in range(len(nums)-1):
            check_nums.append(nums[i+1]-nums[i])
        num_lists.append(check_nums[-1])
        nums = check_nums
    total += num_lists[0] + sum(num_lists[1:])
    num_lists = []
print(total)


