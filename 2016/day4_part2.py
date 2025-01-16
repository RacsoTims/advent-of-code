# URL: https://adventofcode.com/2016/day/4
# Answer:   267

import re

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day4_input.txt"
length_checksum = 5

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
            encrypted_name = parts[0]
            deciphered_signs = []
            for sign in encrypted_name:
                if sign == "-":
                    deciphered_signs.append(" ")
                else:
                    rotations = sector_ID
                    new_letter = chr((ord(sign) - ord('a') + rotations) % 26 + ord('a'))
                    deciphered_signs.append(new_letter)
            deciphered_name = "".join(deciphered_signs)
            with open("C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day4_ouput.txt", "a") as output:
                output.write(f"Name: {deciphered_name}\tSector ID: {sector_ID}\n")
