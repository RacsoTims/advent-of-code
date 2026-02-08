# URL:		https://adventofcode.com/2015/day/7
# Answer:	46065

import numpy as np
import re
import os
puzzle_input = '.\\day7_input.txt'
example_input = '.\\day7_example.txt'
if os.name == 'posix':
	puzzle_input = './day7_input.txt'
	example_input = './day7_example.txt'

bits = 16
wires = {}
live_wires = []

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
    if r"\d+" not in groups[0]:
        if groups[0] not in wires:
            wires[groups[0]] = 0
        wires[groups[1]] = wires[groups[0]]
    else:
        wires[groups[1]] = groups[0]


def complement(groups):
    if groups[0] not in wires:
        wires[groups[0]] = 0
    wires[groups[1]] = calculate_bitwise_complement(wires[groups[0]])


def conjunction(groups):
    if groups[0] == 1:
        if groups[1] not in wires:
            wires[groups[1]] = 0
        wires[groups[2]] = calculate_bitwise_AND(groups[0], wires[groups[1]])
    else:
        for wire in [groups[0], groups[1]]:
            if wire not in wires:
                wires[wire] = 0
        wires[groups[2]] = calculate_bitwise_AND(wires[groups[0]], wires[groups[1]])


def disjunction(groups):
    for wire in [groups[0], groups[1]]:
        if wire not in wires:
            wires[wire] = 0
    wires[groups[2]] = calculate_bitwise_OR(wires[groups[0]], wires[groups[1]])


def left_shift(groups):
    if groups[0] not in wires:
        wires[groups[0]] = 0
    wires[groups[2]] = calculate_left_shift(wires[groups[0]], groups[1])


def right_shift(groups):
    if groups[0] not in wires:
        wires[groups[0]] = 0
    wires[groups[2]] = calculate_right_shift(wires[groups[0]], groups[1])


def execute_instruction(instruction):
    if "NOT" in instruction:
        result = re.search(r"NOT\s([a-z]+)\s->\s([a-z]+)", instruction).groups()
        complement(result)
    elif "AND" in instruction:
        result = re.search(r"([a-z]+|1)\sAND\s([a-z]+)\s->\s([a-z]+)", instruction).groups()
        conjunction(result)
    elif "OR" in instruction:
        result = re.search(r"([a-z]+)\sOR\s([a-z]+)\s->\s([a-z]+)", instruction).groups()
        disjunction(result)
    elif "LSHIFT" in instruction:
        result = re.search(r"([a-z]+)\sLSHIFT\s(\d+)\s->\s([a-z]+)", instruction).groups()
        left_shift(result)
    elif "RSHIFT" in instruction:
        result = re.search(r"([a-z]+)\sRSHIFT\s(\d+)\s->\s([a-z]+)", instruction).groups()
        right_shift(result)
    elif len(re.findall(r"^[a-z]+", instruction)) > 0:
        result = re.search(r"([a-z]+)\s->\s([a-z]+)", instruction).groups()
        assign_value_directly(result)
    else:
        result = re.search(r"(\d+)\s->\s([a-z]+)", instruction).groups()
        assign_value_directly(result)


with open(puzzle_input, 'r') as data:
    for instruction in data.readlines():
        # print(instruction)
        execute_instruction(instruction)
wires_sorted = {k: v for k, v in sorted(wires.items(), key=lambda item: item[0])}
print((wires_sorted))
print(wires['a'])

# signal to wire            (\d+)\s->\s([a-z]+)
# complement to wire        NOT\s([a-z]+)\s->\s([a-z]+)
# AND-gate output to wire   ([a-z]+)\sAND\s([a-z]+)\s->\s([a-z]+)
# OR-gate output to wire    ([a-z]+)\sOR\s([a-z]+)\s->\s([a-z]+)
# left-shift to wire        ([a-z]+)\sLSHIFT\s(\d+)\s->\s([a-z]+)
# right-shift to wire       ([a-z]+)\sRSHIFT\s(\d+)\s->\s([a-z]+)
