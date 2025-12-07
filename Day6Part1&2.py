import math

from Util import fetch_input
import re


def part1(data):

    problems = data.count('+') + data.count('*')

    data = data.split()

    columns = [[] for _ in range(problems)]

    for i, v in enumerate(data):
        columns[i % problems].append(v)

    total_sum = 0
    for column in columns:
        if column[len(column)-1] == '+':
            total_sum += sum( int(s) for s in column[:len(column)-1] )
        else:
            prod = 1
            for s in column[:len(column)-1]:
                prod *= int(s)
            total_sum += prod

    return total_sum


def read_column(col):
    try:
        numbers = []
        for i in range(len(col[0])):
            next = ''.join([e[i] for e in col]).strip()
            numbers.append( next )

        return [ int(nr) for nr in numbers if nr != '']
    except:
        print("Exception occurred: ", col)


def part2(data):
    rows = data.splitlines()
    width = max(len(r) for r in rows)
    matrix = [list(r.ljust(width)) for r in rows]

    total_sum = 0
    numbers = []
    r,c = len(matrix), len(matrix[0])
    for j in range(c - 1, -1, - 1):
        number = ''
        for i in range(0, r - 1):
            number += (matrix[i][j])

        if number.strip() != '':
            numbers.append(int(number))

        if matrix[r-1][j] == '+':
            total_sum += sum(numbers)
            numbers = []
        if matrix[r-1][j] == '*':
            total_sum += math.prod(numbers)
            numbers = []

    return total_sum

data = """12 328  51 64 
45 64  387 23 
 6 98  215 314
*  +   *   +  """

big_data = fetch_input("https://adventofcode.com/2025/day/6/input")

print(part2(data))
print("Compl")
print(part2(big_data))