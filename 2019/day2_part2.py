# URL:		https://adventofcode.com/2019/day/2#part2
# Answer:	7733

import math
import os
puzzle_input = '.\\day2_input.txt'
example_input = '.\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = './day2_input.txt'
	example_input = './day2_example.txt'

add = 1
multiply = 2
halt = 99
noun = 0

target = 19690720
target_reached = False

with open(puzzle_input, 'r') as data:
	program = [int(x) for x in data.read().split(",")]


while not target_reached:
	for verb in range(0, 100):
		memory = program[:]
		memory[1] = noun
		memory[2] = verb
		address = 0
		while memory[address] != halt:
			instruction_pointer = address
			opcode = memory[instruction_pointer]
			parameters = [address+1, address+2, address+3]
			if opcode == add:
				addends = [memory[memory[parameters[0]]], memory[memory[parameters[1]]]]
				memory[memory[parameters[2]]] = sum(addends)
			elif opcode == multiply:
				terms = [memory[memory[parameters[0]]], memory[memory[parameters[1]]]]
				memory[memory[parameters[2]]] = math.prod(terms)
			address += 4
		else:
			if memory[0] == target:
				target_reached = True
				break
	noun += 1
print(100 * (noun-1) + verb)
