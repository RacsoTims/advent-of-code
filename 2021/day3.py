# URL:      https://adventofcode.com/2021/day/3
# Answer:   2967914

import numpy as np

path = "/home/oscar/projects/advent-of-code/2021/day3_input.txt"
bin_gamma = ""
bin_epsilon = ""

def binary_to_decimal(string):
    return sum([(2**(len(string)-i-1) * int(string[i])) for i in range(len(string))])


with open(path, 'r') as puzzle_input:
    report = np.array([list(line.removesuffix("\n")) for line in puzzle_input.readlines()])

for column in report.T:
    zeros = np.count_nonzero(column == "0")
    if zeros > len(column) // 2:
        bin_gamma += "0"
        bin_epsilon += "1"
    else:
        bin_gamma += "1"
        bin_epsilon += "0"

power_consumption = binary_to_decimal(bin_gamma) * binary_to_decimal(bin_epsilon)
print(power_consumption)
