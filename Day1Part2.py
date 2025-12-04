from Util import fetch_input

def increase(x, inc):
    bonus = 0
    full_rotations = inc // 100
    bonus += full_rotations

    inc = inc % 100

    if x + inc > 99:
        return [x + inc - 100, bonus + (1 if x + inc != 100 else 0)]
    else:
        return [x + inc, bonus]

def decrease(x, dec):
    bonus = 0
    full_rotations = dec // 100
    bonus += full_rotations

    dec = dec % 100

    if x - dec < 0:
        return [100 + x - dec, bonus + (1 if x != 0 else 0)]
    else:
        return [x - dec, bonus]

def solve(input):
    x = 50
    c = 0
    for line in input.split("\n"):
        magnitude = int(line[1:])
        x, bonus = increase(x, magnitude) if line[:1] == "R" else decrease(x, magnitude)
        c += bonus
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