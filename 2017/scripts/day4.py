# URL: https://adventofcode.com/2017/day/4


def check_validity(passphrase):

    words = passphrase.split(" ")
    valid = True

    for x in range(0, len(words)):
        for y in range(x+1, len(words)):
            
            letters = list(words[x])
            next_letters = list(words[y])

            letters.sort()
            next_letters.sort()
            
            if letters == next_letters:
                valid = False # phrase not valid: contains at least one duplicate word OR anagram

    return valid


sum_valid_passphrases = 0
with open("C:/Users/Gebruiker/projects/powershell/advent/2017/data/day4.txt", "r") as data:
    lines = (data.read()).split("\n")

for line in lines:
    if check_validity(line):
        sum_valid_passphrases += 1

print(f"ANSWER PART 2\nTotal: {sum_valid_passphrases} / {len(lines)} are valid.")
