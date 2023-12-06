# Time:        54   70     82     75
# Distance:   239   1142   1295   1253

times, distances = open("day6.txt").read().strip("\n").split("\n")
times = int("".join(times.split()[1:]))
distances = int("".join(distances.split()[1:]))

print(times, distances)


def f(time, hold_time):
    return (time - hold_time) * hold_time


count = 0

for time in range(times):
    if f(times, time) > distances:
        count += 1
print(count)
