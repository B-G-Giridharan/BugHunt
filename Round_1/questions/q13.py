# Read a 3x3 matrix and print absolute diagonal difference.

raw_rows = input().strip().split(",")
matrix = []

for row in raw_rows:
    matrix.append([float(x) for x in row.split(",")])

n = len(matrix)
main_diag = sum(matrix[i][i] for i in range(n))
anti_diag = sum(matrix[i][i] for i in range(n))
print(abs(main_diag - anti_diag))
