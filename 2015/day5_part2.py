# URL:      https://adventofcode.com/2015/day/5#part2
# Answer:   69

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day5_input.txt"
count_nice_strings = 0

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


with open(path, "r") as puzzle_input:
    strings_to_test = [string.removesuffix("\n") for string in puzzle_input.readlines()]
    for test_string in strings_to_test:
        if check_str(test_string):
            count_nice_strings += 1
print(count_nice_strings)
