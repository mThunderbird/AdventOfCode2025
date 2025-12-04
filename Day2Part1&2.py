import Util

def checkNumber(number):
    string = str(number)
    length = len(string)
    return string[:(length//2)] == string[(length//2):]

def check_number_part2(number, p):
    if p == len(str(number)):
        return False

    s = str(number)
    l = len(s)

    match = s[0:p]
    for i in range(0,l,p):
        end = i + p
        partition = s[i:end]
        if partition != match:
            return False or check_number_part2(number, p + 1)

    return True

def solve(ranges):
    ranges = ranges.split(",")
    res = 0

    for r in ranges:
        low, high = r.split("-")
        low = int(low)
        high = int(high)
        for i in range(low, high+1):
            if check_number_part2(i, 1):
                res += i

    return res

input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

big_input = Util.fetch_input("https://adventofcode.com/2025/day/2/input")

testNr = 123
print(check_number_part2(testNr, 1))

print(solve(input))
print(solve(big_input))