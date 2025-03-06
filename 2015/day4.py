# URL:		https://adventofcode.com/2015/day/4
# Answer:	282749

import os
import hashlib
puzzle_input = "yzbqklnj"
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2015/day4_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2015/day4_example.txt'

leading_zeroes = 5

def test_key(key) -> bool:
    hash = hashlib.md5(key).hexdigest()
    matching_hash = False
    if hash.startswith("0" * leading_zeroes):
        matching_hash = True
    return matching_hash


for i in range(1, 10_000_000):
	new_key = (puzzle_input + str(i)).encode("utf-8")
	if test_key(new_key):
		print(i)
		break
