# URL:		https://adventofcode.com/2015/day/14
# Answer:	2696

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

with open(puzzle_input, 'r') as data:
    for line in data.read().split("\n"):

        matches = re.findall(regex, line)
        reindeer = Reindeer(matches[0], matches[1], matches[2], matches[3])

        distance = 0
        timer = 0

        while timer < duration_race:
            time_remaining = duration_race - timer
            if time_remaining >= reindeer.duration_flight:
                distance += reindeer.speed * reindeer.duration_flight
            else:
                distance += reindeer.speed * time_remaining
            timer += reindeer.duration_flight + reindeer.duration_rest

        print(f"{reindeer.name} has traveled {distance} km in {duration_race} seconds.")
