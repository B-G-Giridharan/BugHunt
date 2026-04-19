# BUG: Binary search to find target value in sorted array, return index or -1 if not found
import ast

def binary_search(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        if arr[mid] < target: low = mid
        else: high = mid
    return -1

arr, target = ast.literal_eval(input().strip())
result = binary_search(arr, target)
print(result)