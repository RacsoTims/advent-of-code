# URL:		https://adventofcode.com/2015/day/4
# Answer:	282749

import hashlib
import os
puzzle_input = '.\\day4_input.txt'
example_input = '.\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = './day4_input.txt'
	example_input = './day4_example.txt'

puzzle_input = "yzbqklnj"
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
