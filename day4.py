from collections import defaultdict

result = 0
counter = defaultdict(int)
lines = open("day4.txt").read().strip("\n").split("\n")
zeros = []
for i, line in enumerate(lines):
    counter[i] += 1
    game = line.split(":")[-1].strip()
    wc, gc = game.split("|")
    wc = {int(n) for n in wc.split()}
    gc = {int(n) for n in gc.split()}
    winners = len(wc & gc)
    if not winners:
        zeros.append(i)
    for j in range(winners):
        counter[i + 1 + j] += counter[i]
print(sum(counter.values()))
