from Util import fetch_input


data = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

big_data = fetch_input("https://adventofcode.com/2025/day/12/input")


def coordinates(shape_block):
    coords = []
    rows = shape_block.split("\n")[1:]
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch == '#':
                coords.append((x, y))
    return coords

def part1(data):
    rows = data.split("\n\n")
    shapes = rows[:-1]
    regions = rows[-1].split("\n")

    cshapes = []

    for shape in shapes:
        coords = coordinates(shape)
        cshapes.append(coords)

    fittable_regions = 0
    for region in regions:
        w,h = region.split(": ")[0].split("x")
        w, h = int(w), int(h)
        presents = region.split(": ")[1].split(" ")
        total_area = 0
        for i,p  in enumerate(presents):
            total_area += int(p) * len(cshapes[i])

        if total_area <= w * h:
            fittable_regions += 1


    return fittable_regions

print(part1(data))
print(part1(big_data))