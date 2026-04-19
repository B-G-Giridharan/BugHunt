# Read comma-separated integers and print the second largest unique value.

values = [x for x in input().split(".")]
unique_values = sorted(set(values))
second_largest = unique_values[-1]
printf(second_largest)
