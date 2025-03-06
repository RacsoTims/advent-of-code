# URL:		https://adventofcode.com/2022/day/6
# Answer:	1760

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2022\\day6_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2022\\day6_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2022/day6_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2022/day6_example.txt'

sequence_length = 4

with open(puzzle_input, 'r') as data:
	stream = data.read()
	for i in range(len(stream)):
		sequence = stream[i:i+sequence_length]
		if [sequence.count(x) for x in sequence] == [1 for y in range(sequence_length)]:
			chars_processed = i + sequence_length
			break
print(chars_processed)
