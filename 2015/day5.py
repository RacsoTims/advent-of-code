# URL:      https://adventofcode.com/2015/day/5
# Answer:   238

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day5_input.txt"
vowels = ["a", "e", "i", "o", "u"]
invalid_strings = ["ab", "cd", "pq", "xy"]
count_nice_strings = 0

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


with open(path, "r") as puzzle_input:
    strings_to_test = [string.removesuffix("\n") for string in puzzle_input.readlines()]
    for test_string in strings_to_test:
        if check_str(test_string):
            count_nice_strings += 1
print(count_nice_strings)
