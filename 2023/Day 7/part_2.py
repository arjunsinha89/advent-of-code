
with open('sample_input.txt') as file:
    lines = file.readlines()


card_ranks = 'AKQT98765432J'

hand_ranks = ['11111', '11122', '12222', '11333', '22333', '14444', '55555']

hand_rank_map = {
    '11111' : ['11111', '11122'],
    '11122' : ['11122', '11333', '11333'],
    '12222' : ['12222', '22333', '14444'],
    '11333' : ['11333', '14444', '11333', '14444'],
    '22333' : ['22333', '22333', '55555', '55555'],
    '14444' : ['14444', '55555', '14444', '14444', '55555'],
    '55555' : ['55555', '55555', '55555', '55555', '55555', '55555']
}

def get_hand_rank(hand):
    hand_type = []
    num_jokers = 0
    for card in hand:
        card_count = hand.count(card)
        if card == 'J':
            num_jokers += 1
        if card_count > 0:
            hand_type.append(str(card_count))
    hand_type_str = ''.join(sorted(hand_type))
    hand_type_str = hand_rank_map[hand_type_str][num_jokers]
    return hand_ranks.index(hand_type_str)


hands = []
bids = {}

for line in lines:
    line = line.strip('\n').split(' ')
    hands.append(line[0])
    bids[line[0]] = (int(line[1]))
for i in range(len(hands)):
    for j in range(i+1, len(hands)):
        x = get_hand_rank(hands[i])
        y = get_hand_rank(hands[j])
        if x > y:
            temp = hands[i]
            hands[i] = hands[j]
            hands[j] = temp
        elif x == y:
            for k in range(len(hands[i])):
                if card_ranks.index(hands[i][k]) < card_ranks.index(hands[j][k]):
                    temp = hands[i]
                    hands[i] = hands[j]
                    hands[j] = temp
                    break
                elif card_ranks.index(hands[i][k]) > card_ranks.index(hands[j][k]):
                    break

total_winnings = 0
for i in range(len(hands)):
    total_winnings += (i+1)*bids[hands[i]]

print(total_winnings)

