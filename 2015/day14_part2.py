# URL:		https://adventofcode.com/2015/day/14#part2
# Answer:	0

import os
import re
puzzle_input = '.\\day14_input.txt'
example_input = '.\\day14_example.txt'
if os.name == 'posix':
	puzzle_input = './day14_input.txt'
	example_input = './day14_example.txt'


class Reindeer():

    def __init__(self, name, speed, duration_flight,
                 duration_rest, is_flying=True):
        self.name = name
        self.speed = int(speed)
        self.duration_flight = int(duration_flight)
        self.duration_rest = int(duration_rest)
        self.is_flying = is_flying

    # def get_name(self):
    #     return self.name

    # def get_speed(self):
    #     return self.speed

    # def get_duration_flight(self):
    #     return self.duration_flight

    # def get_duration_rest(self):
    #     return self.duration_rest

    # def get_motion_state(self):
    #     return True if self.is_flying else False

    def set_motion_state(self):
        if self.is_flying:
            self.is_flying = False
        else:
            self.is_flying = True
        return True


regex = r"^\w+|\d+"
duration_race = 2503

reindeer = []
distances = {}
points = {}

timers_flying = {}
timers_resting = {}

def award_points():
    farthest = max(distances.values())
    for racer, distance in distances.items():
        if distance == farthest:
            points[racer] += 1


with open(puzzle_input, 'r') as data:
    for line in data.read().split("\n"):
        matches = re.findall(regex, line)
        reindeer.append(Reindeer(matches[0], matches[1], matches[2], matches[3]))
        distances[matches[0]] = 0
        points[matches[0]] = 0

        timers_flying[matches[0]] = 0
        timers_resting [matches[0]] = 0

# print(reindeer)
# print(distances)
# print(points)
# print(timers_flying)
# print(timers_resting)

for sec in range(1, duration_race+1):
    for racer in reindeer:
        if racer.is_flying:
            distances[racer.name] += racer.speed
            timers_flying[racer.name] += 1
            if timers_flying[racer.name] == racer.duration_flight:
                racer.is_flying = False
                timers_flying[racer.name] = 0
        else:
            timers_resting[racer.name] += 1
            if timers_resting[racer.name] == racer.duration_rest:
                racer.is_flying = True
                timers_resting[racer.name] = 0
    award_points()

print(f"Results after {sec} seconds:")
for racer in reindeer:
    print(f"{racer.name} has traveled {distances[racer.name]} km " +
          f"and has been awarded {points[racer.name]} points", end="\n")
# print(points)
