import ast
import json
from collections import defaultdict

def group_anagrams(words):
    res = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))
        res[key].append(w)
    return list(res.values())

words = ast.literal_eval(input().strip())
result = group_anagrams(words)
print(json.dumps(result, separators=(',', ':')), flush=True)