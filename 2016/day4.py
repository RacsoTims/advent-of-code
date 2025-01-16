# URL: https://adventofcode.com/2016/day/4
# Answer:   278221

import re

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day4_input.txt"
sum_sector_IDs = 0
length_checksum = 5
real_rooms = []

def build_checksum(encrypted_name):
    sorted_letters = []
    for letter in encrypted_name:
        if letter not in sorted_letters:
            ranking = 0
            for sorted_letter in sorted_letters:
                occurrences_letter = encrypted_name.count(letter)
                occurrences_sorted_letter = encrypted_name.count(sorted_letter)
                if occurrences_sorted_letter > occurrences_letter:
                    ranking += 1
                elif occurrences_sorted_letter == occurrences_letter and ord(letter) > ord(sorted_letter):
                    ranking += 1
            sorted_letters.insert(ranking, letter)
    checksum = "".join(sorted_letters[:length_checksum])
    return checksum


with open(path, "r") as puzzle_input:
    for line in puzzle_input.readlines():
        parts = re.findall("\\D+\\-|\\d+|\\w+", line)
        encrypted_name = parts[0].replace("-", "")
        sector_ID = int(parts[1])
        given_checksum = parts[-1]
        if build_checksum(encrypted_name) == given_checksum:
            real_rooms.append(sector_ID)
            sum_sector_IDs += sector_ID
print(len(real_rooms))
print(f"Sum of sector IDs = {sum_sector_IDs}")
