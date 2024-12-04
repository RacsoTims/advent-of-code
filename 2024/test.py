import numpy as np

diagonals = []
test = np.array(([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]))
rows, columns = test.shape
for column in range(columns):
    diagonal = ""
    row = 0
    while row < rows and column < columns:
        diagonal += str(test[row, column])
        row += 1
        column += 1
    diagonals.append(diagonal)

print(diagonals)
