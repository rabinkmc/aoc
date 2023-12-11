from collections import deque

graph = open("day11.txt").read().strip("\n").split("\n")
w = len(graph[0])
h = len(graph)
f = open(1, "w")
rr = 0


def build_graph(graph):
    w = len(graph[0])
    h = len(graph)
    rr = 0
    while rr < len(graph):
        for cc in range(w):
            if graph[rr][cc] == "#":
                break
        else:
            graph.insert(rr, graph[rr])
            rr += 1
        rr += 1

    cc = 0
    h = len(graph)
    while cc < len(graph[0]):
        for rr in range(h):
            if graph[rr][cc] == "#":
                break
        else:
            for rr in range(h):
                graph[rr] = graph[rr][0:cc] + "." + graph[rr][cc:]
            cc += 1
        cc += 1


def find_galaxies(graph):
    positions = []
    w = len(graph[0])
    h = len(graph)
    for rr in range(h):
        for cc in range(w):
            if graph[rr][cc] == "#":
                positions.append((rr, cc))

    return positions


build_graph(graph)
w = len(graph[0])
h = len(graph)

locations = find_galaxies(graph)


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
    return abs(r1 - r2) + abs(c1 - c2)


def sum_of_locations(locations=locations):
    total = 0
    points = len(locations[:])
    for i in range(points):
        for j in range(i + 1, points):
            total += dist(locations[i], locations[j])
    return total


print(sum_of_locations())
