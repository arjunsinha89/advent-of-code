with open('input.txt') as file:
    lines = file.readlines()

cards = []

    
sum = 0


for line in lines:
    score = 0
    line = line.strip('\n')
    line = line.split(' ')
    card_num = -1
    my_nums = False
    winning_numbers = []
    ticket_numbers = []
    for num in line:
        if num == '':
            continue
        if num[-1] == ':':
            card_num = int(num[:-1])
        if num == '|':
            my_nums = True
        if num.isdigit():
            if my_nums:
                ticket_numbers.append(int(num))
            else:
                winning_numbers.append(int(num))
    
    card = {'ticket': ticket_numbers, 'winning': winning_numbers, 'count': 1,'cards_won': 0}
    cards.append(card)

        

for i in range(len(cards)):
    cards_won = 0
    for ticket_num in cards[i]['ticket']:
        if ticket_num in cards[i]['winning']:
            cards_won+= 1
    cards[i]['cards_won'] = cards_won


for i in range(len(cards)):
    cards_won = cards[i]['cards_won']
    for j in range(cards_won):
        if (i+j+1) >= len(cards):
            break
        cards[i+j+1]['count'] += cards[i]['count']

for card in cards:
    sum += card['count']
print(sum)

