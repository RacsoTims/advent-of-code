# URL:		https://adventofcode.com/2015/day/19
# Answer:	518

import os
import re

puzzle_input = '.\\day19_input.txt'
example_input = '.\\day19_example.txt'
if os.name == 'posix':
	puzzle_input = './day19_input.txt'
	example_input = './day19_example.txt'

regex = r"\w+"
# starting_molecule = "HOHOHO"
distinct_molecules = []
replacement_rules = {}

with open(puzzle_input, 'r') as data:
	for line in data.read().split("\n"):
		matches = re.findall(regex, line)
		if len(matches) == 1:
			starting_molecule = line
			continue
		elif len(matches) == 2:
			if matches[0] in list(replacement_rules):
				replacement_rules[matches[0]].append(matches[1])
			else:
				replacement_rules[matches[0]] = [matches[1]]

# print(starting_molecule)
# print(replacement_rules)

for i in range(len(starting_molecule)):
	atom = starting_molecule[i]
	try:
		for replace_with in replacement_rules[atom]:
			atoms = list(starting_molecule)
			atoms[i] = replace_with
			molecule = "".join(atoms)
			if molecule not in distinct_molecules:
				distinct_molecules.append(molecule)
	except KeyError:
		try:
			atom = "".join(starting_molecule[i:i+2])
			for replace_with in replacement_rules[atom]:
				atoms = list(starting_molecule)
				del atoms[i:i+2]
				atoms.insert(i, replace_with)
				molecule = "".join(atoms)
				if molecule not in distinct_molecules:
					distinct_molecules.append(molecule)
		except KeyError:
			continue

print(len(distinct_molecules))
