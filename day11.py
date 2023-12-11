graph = open("day11.txt").read().strip("\n").split("\n")


def empty_space(graph):
    empty_rows = [rr for rr, row in enumerate(graph) if all(ch == "." for ch in row)]
    empty_cols = [
        rr for rr, row in enumerate(zip(*graph)) if all(ch == "." for ch in row)
    ]
    return empty_rows, empty_cols


def find_galaxies(graph):
    return [
        (rr, cc)
        for rr, rows in enumerate(graph)
        for cc, ch in enumerate(rows)
        if ch == "#"
    ]


locations = find_galaxies(graph)
empty_rows, empty_cols = empty_space(graph)


def dist(start, end):
    r1, c1 = start
    r2, c2 = end
    c1, c2 = min(c1, c2), max(c1, c2)
    total = 0
    for row in range(r1, r2):
        total += 1000_000 if row in empty_rows else 1
    for col in range(c1, c2):
        total += 1000_000 if col in empty_cols else 1

    return total


def sum_of_locations(locations=locations):
    total = 0
    for i, end in enumerate(locations):
        for start in locations[:i]:
            total += dist(start, end)
    return total


print(sum_of_locations())
