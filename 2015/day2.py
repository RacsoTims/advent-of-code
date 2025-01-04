# URL:      https://adventofcode.com/2015/day/2
# Answer:   1586300

total = 0

with open("C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day2_input.txt", "r") as data:
    boxes = [dimensions_str.removesuffix("\n").split("x") for dimensions_str in data.readlines()]

for box in boxes:
    dimensions = [int(x) for x in box]
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    surface_area = [2*l*w, 2*w*h, 2*h*l]
    slack = min(surface_area) // 2
    total += sum(surface_area) + slack
print(total)
