# URL:		https://adventofcode.com/2015/day/5#part2
# Answer:	69

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day5_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day5_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2015/day5_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2015/day5_example.txt'

nice_strings = 0

def check_for_repeating_letter(test_str) -> bool:
    repeat = False
    for j in range(len(test_str)-2):
        if test_str[j] == test_str[j+2]:
            repeat = True
            break
    return repeat


def check_for_repeating_pair(test_str) -> bool:
    repeat = False
    for j in range(len(test_str)-1):
        pair = test_str[j] + test_str[j+1]
        occurrences = test_str.count(pair)
        if occurrences >= 2:
            repeat = True
            break
    return repeat


def check_str(test_str) -> bool:
    nice = False
    test1 = check_for_repeating_letter(test_str)
    test2 = check_for_repeating_pair(test_str)
    if test1 and test2:
        nice = True
    return nice


with open(puzzle_input, "r") as data:
    strings_to_test = [x.removesuffix("\n") for x in data.readlines()]
    for test_string in strings_to_test:
        if check_str(test_string):
            nice_strings += 1
print(nice_strings)
