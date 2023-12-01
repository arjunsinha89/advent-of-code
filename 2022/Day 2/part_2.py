with open('sample_input.txt') as file:
    lines = file.read().splitlines()

codes = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 0,
    'Y': 3,
    'Z': 6
}


user_choices = {
    (1,0): 3,
    (1,3): 1,
    (1,6): 2,
    (2,0): 1,
    (2,3): 2,
    (2,6): 3,
    (3,0): 2,
    (3,3): 3,
    (3,6): 1
}
score = 0
for line in lines:
    choices = line.split(' ')
    opp_choice = codes[choices[0]]
    result = codes[choices[1]]

    score += result + user_choices[(opp_choice,result)]
print(score)




