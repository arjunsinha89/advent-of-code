
with open('input.txt') as file:
    lines = file.readlines()


card_ranks = 'AKQJT98765432'

hand_ranks = ['11111', '11122', '12222', '11333', '22333', '14444', '55555']

def get_hand_rank(hand):
    hand_type = []
    for card in hand:
        card_count = hand.count(card)
        if card_count > 0:
            hand_type.append(str(card_count))
    hand_type_str = ''.join(sorted(hand_type))
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

