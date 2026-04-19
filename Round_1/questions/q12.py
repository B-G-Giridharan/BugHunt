# Read n and print the nth Fibonacci number (F0=0, F1=1).

n = int(input())
a, b = 1, 1

for _ in range(n):
    a, b = b, a + b

print(a - 1)
