# URL:              https://adventofcode.com/2024/day/1#part2
# Correct answer:   23981443

similarity_score = 0

with open("C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day1_input.txt", "r") as data:
    location_ids = (data.read()).split(None)

list_left = location_ids[::2]
list_right = location_ids[1::2]

for number in list_left:
    similarity_score += int(number) * list_right.count(number)

print(similarity_score)
