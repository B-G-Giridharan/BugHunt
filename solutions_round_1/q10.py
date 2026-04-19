left, right = map(int, input().split(","))
left, right = abs(left), abs(right)
while right:
    left, right = right, left % right
print(left)
