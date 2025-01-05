# URL: https://adventofcode.com/2016/day/1
# Answer:   0

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day1_input.txt"
position = [0,0]   # Santa's position represented as X and Y coordinates
directions = ["N", "E", "S", "W"]
current_direction = directions.index("N")

def execute_turn(turn, direction):
    if turn == "L":
        pass


with open(path, 'r') as puzzle_input:
    instructions = puzzle_input.read().split(", ")

for instruction in instructions:
    turn = instruction[0]
    movement = int(instruction[1])

distance = abs(position[0]) + abs(position[1])
print(distance)
