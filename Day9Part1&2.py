from Util import fetch_input

import heapq

data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

big_data = fetch_input("https://adventofcode.com/2025/day/9/input")

def area(p1, p2):
    return abs((p2[0] - p1[0] + 1)) * abs((p2[1] - p1[1] + 1))

def part1(data):

    red_tiles = [ ( int(r.split(",")[0]), int(r.split(",")[1])) for r in data.split("\n") ]

    sorted_by_x = sorted(red_tiles, key=lambda x: x[0])
    sorted_by_y = sorted(red_tiles, key=lambda x: x[1])

    extreme_x = sorted_by_x[:1000] + sorted_by_y[len(sorted_by_y) - 1000:]
    extreme_y = sorted_by_y[:1000] + sorted_by_x[len(sorted_by_x) - 1000:]

    candidates = set(extreme_x + extreme_y)

    max_area = 0
    for p1 in candidates:
        for p2 in candidates:
            if area(p1, p2) > max_area:
                max_area = area(p1, p2)

    return max_area

def part2(data):

    red_tiles = [ ( int(r.split(",")[0]), int(r.split(",")[1])) for r in data.split("\n") ]

    n = len(red_tiles)
    max_area = 0

    def interior_crossed(x_min, x_max, y_min, y_max):
        for i in range(n):
            r1 = red_tiles[i]
            r2 = red_tiles[(i+1) % n]

            if r1[1] == r2[1]:
                y_edge = r1[1]
                x_edge_start = min(r1[0], r2[0])
                x_edge_end   = max(r1[0], r2[0])
                if y_min < y_edge < y_max and x_edge_end >= x_min and x_edge_start <= x_max:
                    return True

            elif r1[0] == r2[0]:
                x_edge = r1[0]
                y_edge_start = min(r1[1], r2[1])
                y_edge_end   = max(r1[1], r2[1])
                if x_min < x_edge < x_max and y_edge_end >= y_min and y_edge_start <= y_max:
                    return True
        return False

    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            x_min, x_max = min(x1, x2), max(x1, x2)
            y_min, y_max = min(y1, y2), max(y1, y2)

            if x_min == x_max or y_min == y_max:
                continue

            if not interior_crossed(x_min, x_max, y_min, y_max):
                width = x_max - x_min + 1
                height = y_max - y_min + 1
                max_area = max(max_area, width * height)

    return max_area


print(part1(data))
print(part1(big_data))

print(part2(data))
print(part2(big_data))