graph = open("day11.txt").read().strip("\n").split("\n")
w = len(graph[0])
h = len(graph)
f = open(1, "w")
rr = 0


def empty_space(graph):
    empty_rows = []
    empty_cols = []
    w = len(graph[0])
    h = len(graph)
    rr = 0
    while rr < len(graph):
        for cc in range(w):
            if graph[rr][cc] == "#":
                break
        else:
            empty_rows.append(rr)
        rr += 1

    cc = 0
    h = len(graph)
    while cc < len(graph[0]):
        for rr in range(h):
            if graph[rr][cc] == "#":
                break
        else:
            empty_cols.append(cc)
        cc += 1

    return empty_rows, empty_cols


def find_galaxies(graph):
    positions = []
    w = len(graph[0])
    h = len(graph)
    for rr in range(h):
        for cc in range(w):
            if graph[rr][cc] == "#":
                positions.append((rr, cc))

    return positions


# build_graph(graph)
w = len(graph[0])
h = len(graph)

locations = find_galaxies(graph)
empty_rows, empty_cols = empty_space(graph)


def pgraph(graph):
    h = len(graph)
    w = len(graph[0])
    for rr in range(h):
        for cc in range(w):
            f.write(graph[rr][cc])
        f.write("\n")


def dist(start, end):
    r1, c1 = start
    r2, c2 = end
    erows = 0
    ecols = 0
    c1, c2 = min(c1, c2), max(c1, c2)
    for row in empty_rows:
        if r1 < row < r2:
            erows += 1
    for col in empty_cols:
        if c1 <= col <= c2:
            ecols += 1

    r2 += (1000000 * erows - erows) if erows else 0
    c2 += (1000000 * ecols - ecols) if ecols else 0
    ans = abs(r2 - r1) + abs(c2 - c1)
    return ans


def sum_of_locations(locations=locations):
    total = 0
    points = len(locations[:])
    for i in range(points):
        for j in range(i + 1, points):
            total += dist(locations[i], locations[j])
    return total


print(sum_of_locations())
