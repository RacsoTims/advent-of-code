# URL:      https://adventofcode.com/2021/day/3#part2
# Answer:   2967914

import numpy as np

path = "/home/oscar/projects/advent-of-code/2021/day3_input.txt"

def binary_to_decimal(string):
    return sum([(2**(len(string)-i-1) * int(string[i])) for i in range(len(string))])


def filter_for_oxygen_rating(report):
    filtered_report = report
    i = 0
    while filtered_report.shape[0] > 1:
        column = filtered_report.T[i]
        zeros = np.count_nonzero(column == "0")
        ones = np.count_nonzero(column == "1")
        most_common = "0" if zeros > ones else "1"
        filtered_report = filtered_report[filtered_report[:, i] == most_common]
        i += 1
    else:
        return filtered_report


def filter_for_CO2_rating(report):
    filtered_report = report
    i = 0
    while filtered_report.shape[0] > 1:
        column = filtered_report.T[i]
        zeros = np.count_nonzero(column == "0")
        ones = np.count_nonzero(column == "1")
        least_common = "1" if ones < zeros else "0"
        filtered_report = filtered_report[filtered_report[:, i] == least_common]
        i += 1
    else:
        return filtered_report


with open(path, 'r') as puzzle_input:
    report = np.array([list(line.removesuffix("\n")) for line in puzzle_input.readlines()])

bin_oxygen = "".join(filter_for_oxygen_rating(report).flatten())
bin_CO2 = "".join(filter_for_CO2_rating(report).flatten())
life_support_rating = binary_to_decimal(bin_oxygen) * binary_to_decimal(bin_CO2)
print(life_support_rating)
