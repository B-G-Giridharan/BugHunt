import ast
import json

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals)
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if last[1] >= current[0]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

intervals = ast.literal_eval(input().strip())
result = merge_intervals(intervals)
print(json.dumps(result, separators=(',', ':')), flush=True)