with open('input.txt') as file:
    lines = file.read().splitlines()

codes = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

results = {
    -2 : 6,
    -1: 0,
    0: 3,
    1: 6,
    2: 0
}

score = 0
for line in lines:
    choices = line.split(' ')
    opp_choice = codes[choices[0]]
    user_choice = codes[choices[1]]
    score += user_choice + results[(user_choice - opp_choice)]
print(score)







