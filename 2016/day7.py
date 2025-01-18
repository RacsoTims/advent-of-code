# URL: https://adventofcode.com/2016/day/7
# Answer:   105

import re

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day7_input.txt"
tls_supported = 0
groups_of_four_pattern = r"(?=(\w{4}))"
outside_pattern = r"(?=(\w{4}))(?![^\[]*\])"
inside_pattern = r"(?=\[(\w+))"

def check_for_ABBA(list_of_groups):
    abba = False
    for group in list_of_groups:
        if group == group[::-1] and group[0] != group[1]:
            abba = True
            break
    return abba


with open(path, 'r') as puzzle_input:
    for ip in [x.removesuffix("\n") for x in puzzle_input.readlines()]:
        outside_groups = re.findall(outside_pattern, ip)
        inside_groups = re.findall(groups_of_four_pattern, "".join(re.findall(inside_pattern, ip)))
        if check_for_ABBA(outside_groups) == True and check_for_ABBA(inside_groups) == False:
            tls_supported += 1
print(tls_supported)
