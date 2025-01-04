# URL:      https://adventofcode.com/2015/day/1#part2
# Answer:   1795

floor = 0

with open("C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day1_input.txt", "r") as data:
    directions = data.read()
    for i in range(len(directions)):
        if directions[i] == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print(i+1)
            break
