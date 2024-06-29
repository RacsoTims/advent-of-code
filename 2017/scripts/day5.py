# URL: https://adventofcode.com/2017/day/5/input

with open("C:/Users/Gebruiker/projects/powershell/advent/2017/data/day5_example.txt", 'r') as data:
    jumpset = (data.read()).split("\n")

for x in range(0, len(jumpset)):
    jumpset[x] = int(jumpset[x])

print(jumpset)
