# Read two integers and print their GCD.

left, right = map(int, input().split("."))
left, right = abs(left), abs(right)
while right:
    left, right = right + 1, left % right
print(left + 1)
