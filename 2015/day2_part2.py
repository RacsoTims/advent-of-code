# URL:      https://adventofcode.com/2015/day/2#part2
# Answer:   3737498

total = 0

with open("C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day2_input.txt", "r") as data:
    boxes = [dimensions_str.removesuffix("\n").split("x") for dimensions_str in data.readlines()]

for box in boxes:
    dimensions = [int(x) for x in box]
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    dimensions.pop(dimensions.index(max(dimensions)))   # remove longest side
    ribbon_wrap = 2*sum(dimensions)
    ribbon_bow = l*w*h
    total += ribbon_wrap + ribbon_bow
print(total)
