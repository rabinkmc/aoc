data = open("day5.txt").read().split("\n\n")
seeds, *others = data
seeds = [*map(int, seeds.split()[1:])]
ranges = []
for range_data in others:
    rngs = [[*map(int, rng.split())] for rng in range_data.strip("\n").split("\n")[1:]]
    ranges.append(rngs)


def location(source):
    for rngs in ranges:
        for d, s, r in rngs:
            if s <= source < s + r:
                source = d + (source - s)
                break
    return source


def part2(seeds):
    pairs = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    minimum = float("inf")
    for start, end in pairs:
        for seed in range(start, end):
            minimum = min(minimum, location(seed))
    return minimum


print(part2(seeds))
