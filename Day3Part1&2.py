import Util


def joltage_in_line_part1(line):

    n = len(line)
    # precompute max from left for every point
    # precompute max from right for every point
    # Find biggest joltage
    left = [0 for x in range(n)]
    right = [0 for x in range(n)]
    left[0] = int(line[0])
    for i in range(1, n):
        if int(line[i]) > left[i - 1]:
            left[i] = int(line[i])
        else:
            left[i] = left[i - 1]

    right[n-1] = int(line[n-1])
    for i in range(n - 2, -1, -1):
        if int(line[i]) > right[i + 1]:
            right[i] = int(line[i])
        else:
            right[i] = right[i + 1]

    max_joltage = 0
    for i in range(0, n - 1):
        if  max_joltage < left[i] * 10 + right[i + 1]:
            max_joltage = left[i] * 10 + right[i + 1]

    return max_joltage


def joltage_in_line_part2(line):
    n = len(line)
    # I'm feeling Greedy
    # Take the biggest number such that there are at least 12 remaining
    # Repeat until there are exactly the amount you need, and add them all

    joltage = ""
    curr = 0

    while len(joltage) < 12:
        subset = line[curr : n - 11 + len(joltage)]
        max_letter = max([letter for letter in subset])
        joltage += max_letter
        curr = curr + subset.index(max_letter) + 1
    return int(joltage)

def solve(input):

    return  sum([joltage_in_line_part2(line) for line in input.split('\n')])

input = """987654321111111
811111111111119
234234234234278
818181911112111"""

big_input = Util.fetch_input("https://adventofcode.com/2025/day/3/input")

print(solve(input))
print(solve(big_input))