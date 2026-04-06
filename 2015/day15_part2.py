# URL:		https://adventofcode.com/2015/day/15#part2
# Answer:	15862900

from itertools import combinations_with_replacement
from math import prod
import os
import re

puzzle_input = '.\\day15_input.txt'
example_input = '.\\day15_example.txt'
if os.name == 'posix':
	puzzle_input = './day15_input.txt'
	example_input = './day15_example.txt'

regex = r"\w+|\-\d+"
maximum_teaspoons = 100
maximum_calories = 500
maximum_recipe_score = 0
ingredients = []

def calculate_recipe_score(ingredients, teaspoons, ignore_calories=False):
	property_scores = {}
	recipe_score = 0
	for prprty in list(ingredients[0])[1:]:
		prprty_score = 0
		for i in range(len(ingredients)):
			prprty_score += ingredients[i][prprty]*teaspoons[i]
		if prprty_score > 0:
			property_scores[prprty] = prprty_score
		else:
			return recipe_score
	if ignore_calories:
		recipe_score = prod(list(property_scores.values())[:-1])
	else:
		if property_scores["calories"] == maximum_calories:
			recipe_score = prod(list(property_scores.values())[:-1])
	return recipe_score


with open(puzzle_input, 'r') as data:
	for line in data.read().split("\n"):
		mtchs = re.findall(regex, line)
		ingredients.append({"name": mtchs[0], mtchs[1]: int(mtchs[2]),
					  mtchs[3]: int(mtchs[4]), mtchs[5]: int(mtchs[6]),
					  mtchs[7]: int(mtchs[8]), mtchs[9]: int(mtchs[10])})
# print(ingredients)

for ingr_a in range(maximum_teaspoons + 1):
	for ingr_b in range(maximum_teaspoons - ingr_a + 1):
		for ingr_c in range(maximum_teaspoons - ingr_a - ingr_b + 1):
			ingr_d = maximum_teaspoons - ingr_a-  ingr_b - ingr_c
			teaspoons = [ingr_a, ingr_b, ingr_c, ingr_d]
			# print(f"{n} {ingredients[0]["name"]}, {m} {ingredients[1]["name"]}:")
			# print(f"\t{calculate_recipe_score(ingredients, teaspoons)}")
			score = calculate_recipe_score(ingredients, teaspoons)
			# score1 = calculate_recipe_score(ingredients, teaspoons[::-1])
			if score > maximum_recipe_score:
				maximum_recipe_score = score
			# print(teaspoons, maximum_recipe_score)
print(maximum_recipe_score)
