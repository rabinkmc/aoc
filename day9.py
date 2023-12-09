data = open("day9.txt").read().strip("\n").split("\n")

inputs = [[int(n) for n in line.split()] for line in data]


def next_number(sequence):
    sequences = [sequence]
    numbers = sequence
    while not all(num == 0 for num in numbers):
        temp = []
        for i, num in enumerate(numbers[1:]):
            temp.append(num - numbers[i])
        numbers = temp
        sequences.append(numbers)

    sequences[-1].insert(0, 0)
    for index in range(len(sequences) - 1 - 1, -1, -1):
        sequence = sequences[index]
        sequence.insert(0, sequence[0] - sequences[index + 1][0])

    return sequences[0][0]


numbers = [next_number(sequence) for sequence in inputs]
print(sum(numbers))
