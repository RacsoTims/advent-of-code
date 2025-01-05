# URL: https://adventofcode.com/2016/day/1#part2
# Answer:   332

path = "/home/oscar/projects/advent-of-code/2016/day1_input.txt"
positions = []

with open(path, 'r') as puzzle_input:
    instructions = puzzle_input.read().split(", ")

def calculate_distance(instructions):
    x, y = 0, 0     # Santa's position represented as X and Y coordinates
    positions.append((x, y))
    direction_index = 0  # North (0), East (1), South (2), West (3)
    directions_order = ["N", "E", "S", "W"]
    
    move_vector = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)}
    
    for instruction in instructions:
        turn = instruction[0]
        steps = int(instruction[1:])
        
        if turn == 'L':
            direction_index = (direction_index - 1) % 4
        elif turn == 'R':
            direction_index = (direction_index + 1) % 4
        
        current_direction = directions_order[direction_index]
        dx, dy = move_vector[current_direction]
        
        x += dx * steps
        y += dy * steps
        new_position = (x, y)
        positions.append(new_position)
        if positions.count(new_position) == 2:
            break
    
    print(new_position)
    return abs(new_position[0]) + abs(new_position[1])

shortest_distance = calculate_distance(instructions)
print(shortest_distance)
