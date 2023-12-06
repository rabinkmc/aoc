# Time:        54   70     82     75
# Distance:   239   1142   1295   1253

times, distances = open("day6.txt").read().strip("\n").split("\n")
times = [int(n) for n in times.split()[1:]]
distances = [int(n) for n in distances.split()[1:]]


def f(time, hold_time):
    return (time - hold_time) * hold_time


time_dist = zip(times, distances)
result = 1

for max_time, dist in time_dist:
    count = 0
    for t in range(max_time):
        if f(max_time, t) > dist:
            count += 1
    result *= count

print(result)
