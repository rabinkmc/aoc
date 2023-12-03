lines = open("day3.txt").read().strip("\n").split("\n")

MAX_Y = len(lines[0])
MAX_X = len(lines)


def get_top_left(i, j):
    result = ""
    i = i - 1
    line = lines[i]
    j = j - 1
    while 0 <= i <= MAX_X and 0 <= j < MAX_Y and line[j].isdigit():
        result = line[j] + result
        j = j - 1

    return result


def get_top_right(i, j):
    result = ""
    i = i - 1
    line = lines[i]
    j = j + 1
    while 0 <= i <= MAX_X and 0 <= j < MAX_Y and line[j].isdigit():
        result += line[j]
        j = j + 1

    return result


def get_bottom_left(i, j):
    result = ""
    i = i + 1
    line = lines[i]
    j = j - 1
    while 0 <= i <= MAX_X and 0 <= j < MAX_Y and line[j].isdigit():
        result = line[j] + result
        j = j - 1

    return result


def get_bottom_right(i, j):
    result = ""
    i = i + 1
    line = lines[i]
    j = j + 1
    while 0 <= i <= MAX_X and 0 <= j < MAX_Y and line[j].isdigit():
        result += line[j]
        j = j + 1

    return result


def get_left(i, j):
    result = ""
    i = i + 0
    line = lines[i]
    j = j - 1
    while 0 <= j < MAX_Y and line[j].isdigit():
        result = line[j] + result
        j = j - 1

    return result


def get_right(i, j):
    result = ""
    i = i + 0
    line = lines[i]
    j = j + 1
    while 0 <= j < MAX_Y and line[j].isdigit():
        result += line[j]
        j = j + 1

    return result


def adjacent_numbers(i, j):
    top_left = get_top_left(i, j)
    top_right = get_top_right(i, j)
    bottom_left = get_bottom_left(i, j)
    bottom_right = get_bottom_right(i, j)
    left = get_left(i, j)
    right = get_right(i, j)

    top_char = lines[i - 1][j]
    bottom_char = lines[i + 1][j]
    result = []
    if top_left and top_right and top_char.isdigit():
        result.append(int(top_left + top_char + top_right))
    elif top_left and top_char.isdigit():
        result.append(int(top_left + top_char))
    elif top_right and top_char.isdigit():
        result.append(int(top_char + top_right))
    elif top_left and top_right:
        result.extend([int(top_left), int(top_right)])
    elif top_left and not top_right:
        result.append(int(top_left))
    elif top_right and not top_left:
        result.append(int(top_right))

    if bottom_left and bottom_right and bottom_char.isdigit():
        result.append(int(bottom_left + bottom_char + bottom_right))
    elif bottom_left and bottom_char.isdigit():
        result.append(int(bottom_left + bottom_char))
    elif bottom_right and bottom_char.isdigit():
        result.append(int(bottom_char + bottom_right))
    elif bottom_left and bottom_right:
        result.extend([int(bottom_left), int(bottom_right)])
    elif bottom_left and not bottom_right:
        result.append(int(bottom_left))
    elif bottom_right and not bottom_left:
        result.append(int(bottom_right))

    if left:
        result.append(int(left))
    if right:
        result.append(int(right))

    return result[:2]


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


result = []
gears = []
for i, line in enumerate(lines):
    j = 0
    while j < len(line):
        if line[j] == "*":
            numbers = adjacent_numbers(i, j)
            if len(numbers) == 2:
                result.append(numbers[0] * numbers[1])
                gears.append(numbers)
        j = j + 1
print(sum(result))
