from Util import fetch_input

small_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

big_input = fetch_input("https://adventofcode.com/2025/day/5/input")


def part1(data):
    data = data.split("\n")

    ranges = []

    for idx, row in enumerate(data):
        if row == "":
            data = data[idx + 1:]
            break
        a, b = row.split("-")
        ranges.append((int(a), int(b)))

    nr_fresh = 0

    for row in data:
        row = int(row)
        for a, b in ranges:
            if a <= row <= b:
                nr_fresh += 1
                break

    return nr_fresh

print(part1(small_input))
print(part1(big_input))

# def overlaps(interval1, interval2):
#     s1, f1 = interval1
#     s2, f2 = interval2
#     # Assuming f2 > f1 always because of sorting
#     if f1 < s2:
#         return None, 0
#     # How much is the overlap
#     # We know by the sorting that interval2 ends later than interval1
#     #   s2.....f2    or    s2........f2
#     #  s1...f1               s1...f1
#     # overlap = f1 - max(s1,s2)
#     # In the right case, also return the remaining part of interval1
#     if s2 >= s1:
#         # Interval is fully covered to the left
#         return None, max(f1 - s2 + 1, 0)
#     else:
#         # Some remainder to the left
#         return (s2, s1 - 1), max(f1 - s1 + 1, 0)
#
# def part2(data):
#     data = data.split("\n")
#
#     intervals = []
#
#     for row in data:
#         if row == "":
#             break
#         a, b = row.split("-")
#         intervals.append((int(a), int(b)))
#
#     intervals = sorted(intervals, key=lambda x: x[1])
#
#     total_fresh_ids = 0
#
#     for idx, interval in enumerate(intervals):
#         new_ids = max(interval[1] - interval[0] + 1, 0)
#         check = idx - 1
#         while check >= 0 and interval is not None:
#             interval, overlap = overlaps(intervals[check], interval)
#             new_ids -= overlap
#             check -= 1
#
#         total_fresh_ids += new_ids
#
#     return total_fresh_ids

def overlaps(interval1, interval2):
    s1, f1 = interval1
    s2, f2 = interval2
    return not (s1 > f2 or s2 > f1)

def merge(interval1, interval2):
    s1, f1 = interval1
    s2, f2 = interval2
    return min(s1,s2), max(f1,f2)

def part2(data):
    data = data.split("\n")

    intervals = []

    for row in data:
        if row == "":
            break
        a, b = row.split("-")
        intervals.append((int(a), int(b)))

    intervals = sorted(intervals, key=lambda x: x[1])
    final_intervals = []

    for inter in intervals:
        for fin in final_intervals:
            if overlaps(fin, inter):
                final_intervals.remove(fin)
                inter = merge(inter, fin)

        final_intervals.append(inter)

    return sum([f[1] - f[0] + 1 for f in final_intervals])



small_input = """3-5
10-14
16-20
12-18"""

print(part2(small_input))
print(part2(big_input))
# 344795518829269
# 345303532266827
# 345303532266827
# 345995423801866