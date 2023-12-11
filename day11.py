from functools import cached_property


class Graph:
    def __init__(self):
        self.graph = open("day11.txt").read().strip("\n").split("\n")

    @cached_property
    def empty_rows(self):
        return [rr for rr, row in enumerate(self.graph) if all(ch == "." for ch in row)]

    @cached_property
    def empty_cols(self):
        return [
            rr
            for rr, row in enumerate(zip(*self.graph))
            if all(ch == "." for ch in row)
        ]

    @cached_property
    def locations(self):
        return [
            (rr, cc)
            for rr, rows in enumerate(self.graph)
            for cc, ch in enumerate(rows)
            if ch == "#"
        ]

    def dist(self, start, end):
        r1, c1 = start
        r2, c2 = end
        c1, c2 = min(c1, c2), max(c1, c2)
        total = 0

        for row in range(r1, r2):
            total += 1000_000 if row in self.empty_rows else 1
        for col in range(c1, c2):
            total += 1000_000 if col in self.empty_cols else 1

        return total

    def solution(self):
        total = 0
        for i, end in enumerate(self.locations):
            for start in self.locations[:i]:
                total += self.dist(start, end)
        return total


print(Graph().solution())
