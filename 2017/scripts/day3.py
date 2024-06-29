# URL: https://adventofcode.com/2017/day/3

from math import sqrt


def calculate_distance(number):
    if sqrt(number) % 2 == 1:
        distance = int(sqrt(number)) - 1
    else:
        root = int(sqrt(number))    # in order to shorten line 11
        side = root if root % 2 == 0 else root + 1
        offset_abs = (side + 1)**2 - number # 'abs' = absolute
        offset_relative = offset_abs % (side // 2) # in order to shorten line 14
        distance = side - offset_relative if offset_relative != 0 else side - (offset_abs % side)
    return distance


for x in range(1, 26):
    square = f"s:{x}"
    distance = f"d:{calculate_distance(x)}"
    print((square, distance))
