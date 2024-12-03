# URL:              https://adventofcode.com/2024/day/2#part2
# Correct answer:   601

def check_safety(report) -> bool:
    safe = True
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        safe = False
    if not all(diff > 0 for diff in differences) and not all(diff < 0 for diff in differences):
        safe = False
    return safe


def check_safety_with_dampener(report):
    safe_with_dampener = False
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if check_safety(modified_report):
            safe_with_dampener = True
    return safe_with_dampener


with open("C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day2_input.txt", "r") as data:
    lines = (data.read()).splitlines()

count = 0
for line in lines:
    report = list(map(int, line.split()))
    if check_safety(report) or check_safety_with_dampener(report):
        count += 1
print(count)

# Comments
# wat als 'report' een lege lijst is?