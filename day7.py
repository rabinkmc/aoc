from collections import Counter

lines = open("day7.txt").read().strip("\n").split("\n")

cards = []
for line in lines:
    card, bet = line.split()
    cards.append((card, int(bet)))

FIVE_KIND = 6
FOUR_KIND = 5
FULL_HOUSE = 4
THREE_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def strength(hand_bet):
    hand, _ = hand_bet
    jcard = hand
    hand = (
        hand.replace("T", chr(ord("9") + 1))
        .replace("J", chr(ord("2") - 1))
        .replace("Q", chr(ord("9") + 3))
        .replace("K", chr(ord("9") + 4))
        .replace("A", chr(ord("9") + 5))
    )
    j_count = list(jcard).count("J")
    if j_count == 5:
        return FIVE_KIND, hand

    card = ""
    for c in jcard:
        if c != "J":
            card += c

    count = Counter(card)
    common_two = count.most_common(2)
    if len(common_two) == 1:
        return FIVE_KIND, hand
    first = common_two[0][1]
    second = common_two[1][1]
    if first + j_count == 5:
        return FIVE_KIND, hand
    if first + j_count == 4:
        return FOUR_KIND, hand
    if first == 3 and second == 2 or (first == 2 and second == 2 and j_count == 1):
        return FULL_HOUSE, hand
    if first + j_count == 3:
        return THREE_KIND, hand
    if (first == 2 and second == 2) or (first == 2 and j_count == 1):
        return TWO_PAIR, hand
    if first + j_count == 2:
        return ONE_PAIR, hand
    return HIGH_CARD, hand


cards = sorted(cards, key=strength)
sum = 0
for rank, card in enumerate(cards, 1):
    bet = card[1]
    sum += bet * rank
print(sum)
