# URL: https://adventofcode.com/2016/day/9
# Answer:   123

import re

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day9_input.txt"
pattern = r'[A-Z]|\(\d+x\d+\)'
marker_pattern = r'(\d+)x(\d+)'

with open(path, 'r') as puzzle_input:
    data = puzzle_input.read()

decompressed_string = ""
parts = re.findall(pattern, data)
i = 0
while i < len(parts):
    if len(parts[i]) == 1:
        decompressed_string += parts[i]
        i += 1
    else:
        match_numbers = re.search(marker_pattern, parts[i])
        capture_length = int(match_numbers[1])
        repeat = int(match_numbers[2])
        captured_string = "".join(parts[i+1:i+1+capture_length])
        decompressed_string += captured_string[:capture_length] * repeat
        corrected_length = len(re.sub(r'\(\d+x\d+\)', "?", captured_string[:capture_length]))
        i += corrected_length + 1
print(len(decompressed_string))
