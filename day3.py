lines = open("day3.txt").read().strip("\n").split("\n")


def check_partial(i, j):
    directions = [[1, 0], [0, -1], [0, 1], [1, -1], [-1, -1], [-1, 0], [-1, 1], [1, 1]]
    for dx, dy in directions:
        x = i + dx
        y = j + dy
        if 0 <= x < len(lines) and 0 <= y < len(lines[0]):
            if dx == 0 and lines[x][y].isdigit():
                continue

            if lines[x][y] != ".":
                return True

    return False


digits = []
for i, line in enumerate(lines):
    j = 0
    while j < len(line):
        digit = ""
        is_partial = False
        while j < len(line) and line[j].isdigit():
            digit += line[j]
            if check_partial(i, j):
                is_partial = True
            j = j + 1
        if is_partial:
            digits.append(int(digit))
        j = j + 1

print(sum(digits))
