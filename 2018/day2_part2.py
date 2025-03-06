# URL:		https://adventofcode.com/2018/day/2#part2
# Answer:	prtkqyluiusocwvaezjmhmfgx

import os
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2018\\day2_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2018\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2018/day2_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2018/day2_example.txt'

pattern = r'[a-z]'

with open(puzzle_input, 'r') as data:
	raw = data.read()
	boxes = raw.split("\n")
	for i in range(len(boxes)):
		box_ID = boxes[i]
		for j in range(len(boxes[i])):
			search_string = box_ID[:j] + pattern + box_ID[j+1:]
			if len(re.findall(search_string, raw)) == 2:
				common_letters = search_string.replace(pattern, "")
print(common_letters)
