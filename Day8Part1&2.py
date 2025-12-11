import math
from collections import Counter

from Util import fetch_input


class UnionFind:

    sets = []
    rank = []

    def __init__(self, n):
        self.sets = list([i for i in range(n)])
        self.rank = list([1 for i in range(n)])

    def find(self, x):
        if self.sets[x] != x:
            self.sets[x] = self.find(self.sets[x])

        return self.sets[x]

    def union(self, x, y):
        r1 = self.find(x)
        r2 = self.find(y)

        if r1 == r2:
            return False

        if self.rank[r1] == self.rank[r2]:
            self.rank[r1] += 1

        if self.rank[r1] > self.rank[r2]:
            self.sets[r2] = r1
        else:
            self.sets[r1] = r2

        return True



def part1(data):

    rows = [ row.split(",") for row in data.split("\n") ]
    points = [ (int(r[0]), int(r[1]), int(r[2])) for r in rows ]

    edges = list([])
    for i, p1 in enumerate(points):
        for j in range(i + 1, len(points)):
                edges.append((i, j, math.dist(p1, points[j])))

    edges.sort(key=lambda edge: edge[2])

    uf = UnionFind(len(points))
    curr_edge = 0
    while curr_edge < min(len(edges), 1000):
        best_edge = edges[curr_edge]
        curr_edge += 1

        uf.union(best_edge[0], best_edge[1])

    roots = [uf.find(i) for i in range(len(points))]
    clusters = sorted(Counter(roots).values(), reverse=True)

    prod = 1
    for i, c in enumerate(clusters):
        if i > 2:
            break
        prod *= c

    return prod

def part2(data):
    rows = [ row.split(",") for row in data.split("\n") ]
    points = [ (int(r[0]), int(r[1]), int(r[2])) for r in rows ]

    edges = list([])
    for i, p1 in enumerate(points):
        for j in range(i + 1, len(points)):
                edges.append((i, j, math.dist(p1, points[j])))

    edges.sort(key=lambda edge: edge[2])

    uf = UnionFind(len(points))
    mst = []
    curr_edge = 0
    while curr_edge < len(edges) and len(mst) < len(points) - 1:
        best_edge = edges[curr_edge]
        curr_edge += 1
        if uf.union(best_edge[0], best_edge[1]):
            mst.append(best_edge)

    a, b, weight = mst[len(mst)-1]
    return points[a][0] * points[b][0]

data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

big_data = fetch_input("https://adventofcode.com/2025/day/8/input")

print(part1(data))
print(part1(big_data))
print(part2(big_data))