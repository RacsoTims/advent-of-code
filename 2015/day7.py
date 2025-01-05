# URL:      https://adventofcode.com/2015/day/7
# Answer:   377891

import re, numpy as np

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day7_input.txt"
bits = 16
wires = {}

def calculate_bitwise_OR(m, n):
    bin_m = format(int(m), '016b')
    bin_n = format(int(n), '016b')
    result = ""
    for i in range(len(bin_m)):
        if bin_m[i] == bin_n[i] == '0':
            result += '0'
        else:
            result += '1'
    return int(result, 2)


def calculate_bitwise_AND(m, n):
    bin_m = format(int(m), '016b')
    bin_n = format(int(n), '016b')
    result = ""
    for i in range(len(bin_m)):
        if bin_m[i] == bin_n[i] == '1':
            result += '1'
        else:
            result += '0'
    return int(result, 2)


def calculate_bitwise_complement(n):
    return 2**bits + ~int(n)


def calculate_right_shift(n, shift):
    return int(n) >> int(shift)


def calculate_left_shift(n, shift):
    return int(n) << int(shift)


def assign_value_directly(groups):
    wires[groups[1]] = groups[0]


def complement(groups):
    wires[groups[1]] = calculate_bitwise_complement(wires[groups[0]])


def conjunction(groups):
    wires[groups[2]] = calculate_bitwise_AND(wires[groups[0]], wires[groups[1]])


def disjunction(groups):
    wires[groups[2]] = calculate_bitwise_OR(wires[groups[0]], wires[groups[1]])


def left_shift(groups):
    wires[groups[2]] = calculate_left_shift(wires[groups[0]], groups[1])


def right_shift(groups):
    wires[groups[2]] = calculate_right_shift(wires[groups[0]], groups[1])


def execute_instruction(instruction):
    if "NOT" in instruction:
        result = re.search("NOT\s([a-z]+)\s->\s([a-z]+)", instruction).groups()
        complement(result)
    elif "AND" in instruction:
        result = re.search("([a-z]+)\sAND\s([a-z]+)\s->\s([a-z]+)", instruction).groups()
        conjunction(result)
    elif "OR" in instruction:
        result = re.search("([a-z]+)\sOR\s([a-z]+)\s->\s([a-z]+)", instruction).groups()
        disjunction(result)
    elif "LSHIFT" in instruction:
        result = re.search("([a-z]+)\sLSHIFT\s(\d+)\s->\s([a-z]+)", instruction).groups()
        left_shift(result)
    elif "RSHIFT" in instruction:
        result = re.search("([a-z]+)\sRSHIFT\s(\d+)\s->\s([a-z]+)", instruction).groups()
        right_shift(result)
    else:
        result = re.search("(\d+)\s->\s([a-z]+)", instruction).groups()
        assign_value_directly(result)


with open(path, "r") as puzzle_input:
    for instruction in puzzle_input.readlines():
        execute_instruction(instruction)
print(wires)
print(wires['a'])

# signal to wire            (\d+)\s->\s([a-z]+)
# complement to wire        NOT\s([a-z]+)\s->\s([a-z]+)
# AND-gate output to wire   ([a-z]+)\sAND\s([a-z]+)\s->\s([a-z]+)
# OR-gate output to wire    ([a-z]+)\sOR\s([a-z]+)\s->\s([a-z]+)
# left-shift to wire        ([a-z]+)\sLSHIFT\s(\d+)\s->\s([a-z]+)
# right-shift to wire       ([a-z]+)\sRSHIFT\s(\d+)\s->\s([a-z]+)
