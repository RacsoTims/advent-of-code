# URL:      https://adventofcode.com/2021/day/1#part2
# Answer:   1653

path = "/home/oscar/projects/advent-of-code/2021/day1_input.txt"
count = 0
window_size = 3

with open(path, 'r') as puzzle_input:
    measurements = [int(x) for x in puzzle_input.readlines()]
    for i in range(0, len(measurements)-window_size):
        if (sum(measurements[i:i+window_size])) < sum(measurements[i+1:i+window_size+1]):
            count += 1

print(count)
