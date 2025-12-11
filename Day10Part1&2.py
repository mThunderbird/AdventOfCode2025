import numpy as np
from Util import fetch_input

from collections import  deque

from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpInteger

data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


big_data = fetch_input("https://adventofcode.com/2025/day/10/input")

class Machine:
    def __init__(self, row):
        self.target_toggle = []
        self.joltage = []
        self.matrix = []

        row = row.split(" ")
        target = row[0]

        for i in range(1, len(target) - 1):
            self.target_toggle.append(1 if target[i] == "#" else 0)

        for button in row[1:-1]:
            button = button.replace("(", "").replace(")", "")
            toggle_vector = [0] * len(self.target_toggle)
            for number in button.split(","):
                toggle_vector[int(number)] = 1
            self.matrix.append(toggle_vector)

        for j in row[-1].replace("{", "").replace("}", "").split(","):
            self.joltage.append(int(j))

    def part1(self):

        target = np.array(self.target_toggle)
        buttons = np.array(self.matrix)
        n = len(buttons)

        best = None

        for i in range(1 << n):
            combo_bits = [(i >> j) & 1 for j in range(n)]
            presses = sum(combo_bits)


            if best is not None and presses >= best:
                continue

            result = np.zeros(len(target), dtype=int)
            for j in range(n):
                if combo_bits[j] == 1:
                    result = (result + buttons[j]) % 2

            if np.array_equal(result, target):
                best = presses

        return best

    def part2(self):

        num_buttons = len(self.matrix)
        num_counters = len(self.joltage)

        prob = LpProblem("MinimizeButtonPresses", LpMinimize)
        button_vars = [ LpVariable(f'button_{i}', lowBound=0, cat=LpInteger) for i in range(num_buttons) ]
        prob += lpSum(button_vars)

        for j in range(num_counters):
            prob += lpSum(self.matrix[i][j] * button_vars[i] for i in range(num_buttons)) == self.joltage[j]

        prob.solve()

        total_presses = sum( int(button_vars[i].varValue) for i in range(num_buttons) )
        return total_presses

    def __str__(self):
        return f'Machine({self.target_toggle},{self.matrix})'
    def __repr__(self):
        return self.__str__()


def part1(data):

    machines = [ Machine(row) for row in data.split("\n") ]
    results = [ machine.part1() for machine in machines ]

    return sum(results)


def part2(data):

    machines = [ Machine(row) for row in data.split("\n") ]
    results = [ machine.part2() for machine in machines ]

    return sum(results)

print(part1(data))
print(part1(big_data))

print(part2(data))
print(part2(big_data))