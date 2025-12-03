# URL:		https://adventofcode.com/2021/day/3#part2
# Answer:	7041258

import numpy as np
import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

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


with open(puzzle_input, 'r') as data:
	report = np.array([list(line.removesuffix("\n")) for line in data.readlines()])

bin_oxygen = "".join(filter_for_oxygen_rating(report).flatten())
bin_CO2 = "".join(filter_for_CO2_rating(report).flatten())
life_support_rating = binary_to_decimal(bin_oxygen) * binary_to_decimal(bin_CO2)
print(life_support_rating)
