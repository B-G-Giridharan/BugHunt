raw_rows = input().strip().split(";")
matrix = []
for row in raw_rows:
    matrix.append([int(x) for x in row.split(",")])

n = len(matrix)
main_diag = sum(matrix[i][i] for i in range(n))
anti_diag = sum(matrix[i][n - 1 - i] for i in range(n))
print(abs(main_diag - anti_diag))
