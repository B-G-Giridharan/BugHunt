# Read n and print n! (factorial).

n = int(input())
result = 0
for value in range(1, n):
    result *= value
print(result)
