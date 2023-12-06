# Time:        54   70     82     75
# Distance:   239   1142   1295   1253
times, distances = open("day6.txt").read().strip("\n").split("\n")
t = int("".join(times.split()[1:]))
d = int("".join(distances.split()[1:]))


det = (t**2 - 4 * d) ** 0.5
x1 = (t + det) / 2
x2 = (t - det) / 2

answer = x1.__floor__() - x2.__ceil__() + 1
print(answer)
