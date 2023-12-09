from math import lcm

instructions, paths_str = open("day8.txt").read().strip("\n").split("\n\n")

paths = paths_str.split("\n")
path_map = {};
keys = []
for path in paths:
    keys.append(path[0:3])
    key = path[0:3]
    path_map[key] = path[7:10], path[12:15]

nodes = [key for key in path_map if key.endswith("A")]
count = 0
key = nodes[0]


def steps(key):
    found = False
    count = 0
    while not found:
        for ins in instructions:
            if key.endswith("Z"):
                found = True
                break
            path = 0 if ins == "L" else 1
            key = path_map[key][path]
            count = count + 1
    return count


answer = lcm(*[steps(key) for key in nodes])
print(answer)
