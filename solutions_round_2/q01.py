import ast

def remove_odds(nums):
    return [n for n in nums if n % 2 == 0]

nums = ast.literal_eval(input().strip())
result = remove_odds(nums)
print(result, flush=True)