# URL: https://adventofcode.com/2016/day/1#part2
# Answer:   166

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day1_input.txt"
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
        
        current_x_coord = positions[-1][0]
        current_y_coord = positions[-1][1]
        
        if x < 0:
            for n in range(current_x_coord - 1, current_x_coord + x - 1, -1):
                if (n, current_y_coord) in positions:
                    return abs(n) + abs(current_y_coord)
                else:
                    positions.append((n, current_y_coord))
        if x > 0:
            for m in range(current_x_coord + 1, current_x_coord + x + 1):
                if (m, current_y_coord) in positions:
                    return abs(m) + abs(current_y_coord)
                else:
                    positions.append((m, current_y_coord))
        if y < 0:
            for o in range(current_y_coord - 1 , current_y_coord + y - 1, -1):
                if (current_x_coord, o) in positions:
                    return abs(current_x_coord) + abs(o)
                else:
                    positions.append((current_x_coord, o))
        if y > 0:
            for p in range(current_y_coord + 1 , current_y_coord + y + 1):
                if (current_x_coord, p) in positions:
                    print(current_x_coord, p)
                    return abs(current_x_coord) + abs(p)
                else:
                    positions.append((current_x_coord, p))
        x = 0
        y = 0


shortest_distance = calculate_distance(instructions)
print(shortest_distance)
