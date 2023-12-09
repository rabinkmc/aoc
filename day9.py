data = open("day9.txt").read().strip("\n").split("\n")

inputs = [[int(n) for n in line.split()] for line in data]


def next_num(seq):
    if all(num == 0 for num in seq):
        return 0
    diff = [n - seq[i] for i, n in enumerate(seq[1:])]
    return seq[-1] + next_num(diff)


print(sum(next_num(seq) for seq in inputs))
