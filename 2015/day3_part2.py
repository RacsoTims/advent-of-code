# URL:      https://adventofcode.com/2015/day/3#part2
# Answer:   2360

locations_visited = []
position_santa= [0,0]       # Santa's position on the grid given as coordinates (X, Y)
position_robot = [0,0]      # Robo-Santa's position on the grid given as coordinates (X, Y)
locations_visited.append(position_santa)

def move(position, direction) -> list:
    new_position = position[:]
    if direction == "^":
        new_position[1] += 1
    elif direction == "v":
        new_position[1] -= 1
    elif direction == ">":
        new_position[0] += 1
    else:
        new_position[0] -= 1
    return new_position


def check_if_visited(position) -> bool:
    visited_before = position in locations_visited
    return visited_before


with open("C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day3_input.txt", "r") as data:
    directions = data.read()

for i in range(len(directions)):
    if i % 2 == 0:
        position_robot = move(position_robot, directions[i])
        if not check_if_visited(position_robot):
            locations_visited.append(position_robot)
    else:
        position_santa = move(position_santa, directions[i])
        if not check_if_visited(position_santa):
            locations_visited.append(position_santa)

print(len(locations_visited))
