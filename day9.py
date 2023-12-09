data = open("day9.txt").read().strip("\n").split("\n")

inputs = [[int(n) for n in line.split()] for line in data]


def next_number(sequence):
    if all(num == 0 for num in sequence):
        return 0
    temp = []
    for i, num in enumerate(sequence[1:]):
        temp.append(num - sequence[i])
    return sequence[-1] + next_number(temp)


print(sum(next_number(sequence) for sequence in inputs))
