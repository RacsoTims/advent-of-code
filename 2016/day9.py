# URL: https://adventofcode.com/2016/day/9
# Answer:   123

import re

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day9_input.txt"
marker_pattern = r'\((\d+)x(\d+)\)'

with open(path, 'r') as puzzle_input:
    data = [x.removesuffix("\n") for x in puzzle_input.readlines()]

for datum in data:
    capture = False
    decompressed_string = ""
    for i in range(len(datum)):
        if not capture:
            decompressed_string += datum[i]
        elif datum[i] == "(" and not capture:
            capture = True
            marker = re.search(marker_pattern)
            marker_length = len(marker.group(0))
            subsequent_chars = marker.group(1)
            repeat = marker.group(2)
        else:
            continue
    print(decompressed_string)
# print(data)
