from Util import  fetch_input


def solve(input, r, c):

    cleared_input = input[:]
    total_available_papers = 0

    for i in range(r):
        for j in range(c):

            if input[i * c + j] != '@':
                continue

            dx = [-1, -1, -1, 0, 0, 1, 1, 1]
            dy = [-1, 0, +1, -1, +1, -1, 0, +1]
            papers_around = 0
            for k in range(8):
                if 0 <= i + dx[k] < r and 0 <= j + dy[k] < c:
                    idx = (i + dx[k]) * c + j + dy[k]
                    if input[idx] == '@':
                        papers_around += 1

            if papers_around < 4:
                total_available_papers += 1
                cleared_input = cleared_input[:i * c + j] + '.' + cleared_input[i * c + j + 1:]

    return total_available_papers, cleared_input

input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

big_input = fetch_input("https://adventofcode.com/2025/day/4/input")

def part1(input):

    r = len(input.split('\n'))
    c = len(input) // r
    input = input.replace('\n', '')

    return solve(input, r, c)[0]

print(part1(input))
print(part1(big_input))

def part2(input):
    r = len(input.split('\n'))
    c = len(input) // r
    input = input.replace('\n', '')

    res = solve(input, r, c)
    removed = res[0]
    while res[0] > 0:
        res = solve(res[1], r, c)
        removed += res[0]
    return removed

print(part2(input))
print(part2(big_input))