# URL:      https://adventofcode.com/2015/day/1
# Answer:   74

with open("C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day1_input.txt", "r") as data:
    directions = data.read()
    floor = directions.count("(") - directions.count(")")
print(floor)
