# URL:		https://adventofcode.com/2023/day/5
# Answer:	340994526

import re
import os
puzzle_input = '.\\day5_input.txt'
example_input = '.\\day5_example.txt'
if os.name == 'posix':
	puzzle_input = './day5_input.txt'
	example_input = './day5_example.txt'

def map_to_int(lst) -> list:
	return list(map(int, lst))


def look_up_dest(source, dict) -> int:
	dest = 0
	mapping = False
	for entry in dict.values():
		dest_range_start = entry[0]
		source_range_start = entry[1]
		range_length = entry[2]
		if source in range(source_range_start, source_range_start + range_length):
			dest = dest_range_start + (source - source_range_start)
			mapping = True
			break
	return dest if mapping else source


seed_to_soil_map = {}
soil_to_fertilizer_map = {}
fertilizer_to_water_map = {}
water_to_light_map = {}
light_to_temperature_map = {}
temperature_to_humidity_map = {}
humidity_to_location_map = {}

all_maps = []
all_seeds_info = []

lowest_location = float('inf')

with open(puzzle_input, 'r') as data:
	for section in re.split(r'\n\n', data.read()):
		if "seeds" in section:
			seeds = map_to_int(re.split(r'\s', section)[1:])
		elif "seed-to-soil" in section:
			entries = re.split(r'\n', section)[1:]
			for i in range(len(entries)):
				seed_to_soil_map[i] = map_to_int(re.split(r'\s', entries[i]))
			all_maps.append(seed_to_soil_map)
		elif "soil-to-fertilizer" in section:
			entries = re.split(r'\n', section)[1:]
			for i in range(len(entries)):
				soil_to_fertilizer_map[i] = map_to_int(re.split(r'\s', entries[i]))
			all_maps.append(soil_to_fertilizer_map)
		elif "fertilizer-to-water" in section:
			entries = re.split(r'\n', section)[1:]
			for i in range(len(entries)):
				fertilizer_to_water_map[i] = map_to_int(re.split(r'\s', entries[i]))
			all_maps.append(fertilizer_to_water_map)
		elif "water-to-light" in section:
			entries = re.split(r'\n', section)[1:]
			for i in range(len(entries)):
				water_to_light_map[i] = map_to_int(re.split(r'\s', entries[i]))
			all_maps.append(water_to_light_map)
		elif "light-to-temperature" in section:
			entries = re.split(r'\n', section)[1:]
			for i in range(len(entries)):
				light_to_temperature_map[i] = map_to_int(re.split(r'\s', entries[i]))
			all_maps.append(light_to_temperature_map)
		elif "temperature-to-humidity" in section:
			entries = re.split(r'\n', section)[1:]
			for i in range(len(entries)):
				temperature_to_humidity_map[i] = map_to_int(re.split(r'\s', entries[i]))
			all_maps.append(temperature_to_humidity_map)
		elif "humidity-to-location" in section:
			entries = re.split(r'\n', section)[1:]
			for i in range(len(entries)):
				humidity_to_location_map[i] = map_to_int(re.split(r'\s', entries[i]))
			all_maps.append(humidity_to_location_map)
# print(seeds)
# print(seed_to_soil_map)
# print(soil_to_fertilizer_map)
# print(fertilizer_to_water_map)
# print(water_to_light_map)
# print(light_to_temperature_map)
# print(temperature_to_humidity_map)
# print(humidity_to_location_map)
# print(len(all_maps), all_maps)
for seed in seeds:
	seed_info = {"seed": seed, "soil": 0, "fertilizer": 0, "water": 0,
			"light": 74, "temperature": 0, "humidity": 0, "location": 0}
	for i in range(len(all_maps)):
		seed_info[list(seed_info.keys())[i+1]] = look_up_dest(seed_info[list(seed_info.keys())[i]], all_maps[i])
	lowest_location = seed_info['location'] if seed_info['location'] < lowest_location else lowest_location
	all_seeds_info.append(seed_info)
	# print(seed_info)
# print(all_seeds_info)
print(lowest_location)
