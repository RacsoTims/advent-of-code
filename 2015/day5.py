# URL:		https://adventofcode.com/2015/day/5
# Answer:	238

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day5_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day5_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2015/day5_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2015/day5_example.txt'

vowels = ["a", "e", "i", "o", "u"]
invalid_strings = ["ab", "cd", "pq", "xy"]
nice_strings = 0

def count_vowels(test_str) -> bool:
    count = 0
    for i in range(len(test_str)):
        if test_str[i] in vowels:
            count += 1
    if count >= 3:
        return True
    else:
        return False


def check_for_repeating_letter(test_str) -> bool:
    repeat = False
    for j in range(len(test_str)-1):
        if test_str[j] == test_str[j+1]:
            repeat = True
            break
    return repeat


def check_for_invalid_strings(test_str) -> bool:
    no_invalid_string = True
    for invalid in invalid_strings:
        if invalid in test_str:
            no_invalid_string = False
            break
    return no_invalid_string


def check_str(test_str) -> bool:
    nice = False
    test0 = count_vowels(test_str)
    test1 = check_for_repeating_letter(test_str)
    test2 = check_for_invalid_strings(test_str)
    if test0 and test1 and test2:
        nice = True
    return nice


with open(puzzle_input, 'r') as data:
	strings_to_test = [x.removesuffix("\n") for x in data.readlines()]
	for test_string in strings_to_test:
		if check_str(test_string):
			nice_strings += 1
print(nice_strings)
