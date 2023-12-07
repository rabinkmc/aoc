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


def get_score(hand):
    jcard = hand
    j_count = list(jcard).count("J")
    if j_count == 5:
        return FIVE_KIND

    card = ""
    for c in jcard:
        if c != "J":
            card += c

    count = Counter(card)
    common_two = count.most_common(2)
    if len(common_two) == 1:
        return FIVE_KIND
    first = common_two[0][1]
    second = common_two[1][1]
    if first + j_count == 5:
        return FIVE_KIND
    if first + j_count == 4:
        return FOUR_KIND
    if first == 3 and second == 2 or (first == 2 and second == 2 and j_count == 1):
        return FULL_HOUSE
    if first + j_count == 3:
        return THREE_KIND
    if (first == 2 and second == 2) or (first == 2 and j_count == 1):
        return TWO_PAIR
    if first + j_count == 2:
        return ONE_PAIR
    return HIGH_CARD


def compare_order(hand1, hand2):
    face_cards = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    for a, b in zip(hand1, hand2):
        if a == b:
            continue
        val_c1 = face_cards.get(a) or int(a)
        val_c2 = face_cards.get(b) or int(b)
        return val_c1 > val_c2
    return 0


def compare(c1, c2):
    s1 = get_score(c1[0])
    s2 = get_score(c2[0])
    if s1 == s2:
        return compare_order(c1[0], c2[0])
    return s1 > s2


for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        if compare(cards[i], cards[j]):
            cards[j], cards[i] = cards[i], cards[j]

sum = 0
for rank, card in enumerate(cards, 1):
    bet = card[1]
    sum += bet * rank
print(sum)
