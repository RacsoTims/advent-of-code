# URL: https://adventofcode.com/2016/day/5
# Answer:   4543c154

import hashlib

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day5_input.txt"
leading_zeros = 5
password = ""

def get_md5_of_string(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()


with open(path, "r") as puzzle_input:
    door_ID = puzzle_input.read()

for i in range(12_000_000):
    string_to_hash = door_ID + str(i)
    hash = get_md5_of_string(string_to_hash)
    if hash[:leading_zeros] == leading_zeros * "0":
        password += hash[5] #'If it does, the sixth character in the hash is the next character of the password.'
    if len(password) == 8:
        break
print(password)
