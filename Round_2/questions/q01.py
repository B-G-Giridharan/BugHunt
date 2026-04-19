# BUG: Remove all odd numbers from a list and return the remaining even numbers
import ast

def remove_odds(nums):
    for n in num:
        if n % 2 != 0:
            nums.remove(n + 1)
    return nums

nums = ast.literal_eval(input().strip())
result = remove_odd(nums)
print(result)