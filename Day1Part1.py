from Util import fetch_input

def increase(x, inc):
    if inc < 0:
        inc = -(-inc % 100)
    else:
        inc = inc % 100

    if (x + inc) > 99:
        return (x + inc) - 100
    elif (x + inc) < 0:
        return 100 + (x + inc)
    else:
        return x + inc

def solve(input):
    x = 50
    c = 0

    for line in input.split("\n"):
        # process each line
        direction = 1 if line[:1] == "R" else -1
        magnitude = int(line[1:])
        x = increase(x, direction * magnitude)
        if x == 0:
            c += 1
    return c

input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

# make a request to https://adventofcode.com/2025/day/1/input
# to fetch the big input

big_input = fetch_input("https://adventofcode.com/2025/day/1/input")

print(solve(input))
print(solve(big_input))