values = [int(x) for x in input().split(",")]
unique_values = sorted(set(values))
print(unique_values[-2])
