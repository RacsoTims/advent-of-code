# URL: https://adventofcode.com/2016/day/5#part2
# Answer:   1050cbbd

import hashlib

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day5_input.txt"
leading_zeros = 5
password = ""
password_length = 8
indexes = ["_" for x in range(password_length)]

def get_md5_of_string(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()


with open(path, "r") as puzzle_input:
    door_ID = puzzle_input.read()

for i in range(30_000_000):
    string_to_hash = door_ID + str(i)
    hash = get_md5_of_string(string_to_hash)
    if hash[:leading_zeros] == leading_zeros * "0":
        try:
            index = int(hash[5]) # 'the sixth character represents the position (0-7)'
        except(ValueError):
            continue
        if index < 8 and indexes[index] == "_":
            indexes[index] = hash[6]  # 'and the seventh character is the character to put in that position.'
    if len(password) == password_length:
        break
password = "".join(indexes)
print(password)
