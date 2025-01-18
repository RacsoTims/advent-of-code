# URL: https://adventofcode.com/2016/day/7#part2
# Answer:   166

import re

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day7_input.txt"
ssl_supported = 0
groups_of_four_pattern = r"(?=(\w{3}))"
outside_pattern = r"(?=(\w{3}))(?![^\[]*\])"
inside_pattern = r"(?=\[(\w+))"

def check_for_ABA(outside_groups):
    aba = []
    for group in outside_groups:
        if group[0] != group[1] and group[0] == group[2]:
            aba.append(group)
    return aba


def check_for_BAB(inside_groups, aba):
    bab = False
    for aba_pattern in aba:
        letters = list(aba_pattern)
        bab_pattern = letters[1] + letters[0] + letters[1]
        if bab_pattern in inside_groups:
            bab = True
            break
    return bab


with open(path, 'r') as puzzle_input:
    for ip in [x.removesuffix("\n") for x in puzzle_input.readlines()]:
        outside_groups = re.findall(outside_pattern, ip)
        inside_groups = re.findall(groups_of_four_pattern, "".join(re.findall(inside_pattern, ip)))
        if len(check_for_ABA(outside_groups)) > 0:
            if check_for_BAB(inside_groups, check_for_ABA(outside_groups)):
                ssl_supported += 1
print(ssl_supported)
