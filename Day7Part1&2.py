from Util import fetch_input

def part1(data):
    data = [list(row) for row in data.split("\n")]
    indices = [ (0, data[0].index("S"))]

    splits = 0
    while len(indices) > 0:
        row, col = indices.pop(0)
        if row == len(data) - 1:
            continue

        if data[row + 1][col] == ".":
            data[row + 1][col] = "|"
            indices.append((row + 1, col))
        elif data[row + 1][col] == "^":
            splits += 1
            if col - 1 >= 0 and data[row + 1][col - 1] == ".":
                data[row + 1][col - 1] = "|"
                indices.append((row + 1, col - 1))

            if col + 1 < len(data[row + 1]) and data[row + 1][col + 1] == ".":
                data[row + 1][col + 1] = "|"
                indices.append((row + 1, col + 1))

    return splits

def part2(data):
    data = [list(row) for row in data.split("\n")]
    indices = [(0, data[0].index("S"))]

    paths = [ list([ 0 for _ in range(len(data[i])) ]) for i in range(len(data))]
    paths[0][indices[0][1]] = 1

    total_paths = 0

    while len(indices) > 0:
        row, col = indices.pop(0)
        if row == len(data) - 1:
            total_paths += paths[row][col]
            continue

        if data[row + 1][col] != "^":
            if data[row + 1][col] == ".":
                data[row + 1][col] = "|"
                indices.append((row + 1, col))
            paths[row+1][col] += paths[row][col]

        else:
            if col - 1 >= 0 and data[row + 1][col - 1] != "^":
                if data[row + 1][col - 1] == ".":
                    data[row + 1][col - 1] = "|"
                    indices.append((row + 1, col - 1))
                paths[row + 1][col - 1] += paths[row][col]
            else:
                total_paths += paths[row][col]

            if col + 1 < len(data[row + 1]) and data[row + 1][col + 1] != "^":
                if data[row + 1][col + 1] == ".":
                    data[row + 1][col + 1] = "|"
                    indices.append((row + 1, col + 1))
                paths[row + 1][col + 1] += paths[row][col]
            else:
                total_paths += paths[row][col]

    return total_paths

data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

big_data = fetch_input("https://adventofcode.com/2025/day/7/input")

print(part1(data))
print(part1(big_data))

print(part2(data))
print(part2(big_data))