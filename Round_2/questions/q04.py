# BUG: Merge overlapping intervals while preserving the maximum end value for overlap
import ast
import json

def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for i in intervals:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = i[1]
    return merged

intervals = ast.literal_eval(input().strip())
result = merge_intervals(intervals)
print(json.dumps(result, separators=(',', ':')))