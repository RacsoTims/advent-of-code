# URL:		https://adventofcode.com/2023/day/5
# Answer:	0

import re
import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2023\\day5_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2023\\day5_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2023/day5_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2023/day5_example.txt'

seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}

seed_to_all_properties = {}
properties = 7	# 0 = soil, 1 = fertilizer, 2 = water, 3 = light, 4 = temperature, 5 = humidity, 6 = location

with open(example_input, 'r') as data:
	seeds_and_mappings = data.readlines()
for i in range(len(seeds_and_mappings)):
	line = seeds_and_mappings[i]
	if "seeds:" in line:
		seeds = re.findall(r'\d+', line)
		for seed in seeds:
			seed_to_all_properties[seed] = [seed for x in range(properties)]
	elif "seed_to_soil" in line:
		pass
	elif "soil_to_fertilizer" in line:
		pass
	elif "fertilizer_to_water" in line:
		pass
	elif "water_to_light" in line:
		pass
	elif "light_to_temperature" in line:
		pass
	elif "temperature_to_humidity" in line:
		pass
	elif "humidity_to_location" in line:
		pass
print(seed_to_all_properties)
