# BUG: Group anagrams from a list of words (words with same letters grouped together)
import ast
import json

def group_anagrams(words):
    res = {}
    for w in words:
        s = sorted(w)
        if s in res: res[s].append(w)
        else: res[s] = [w]
    return list(res.values())

words = ast.literal_eval(input().strip())
result = group_anagrams(words)
print(json.dumps(result, separators=(',', ':')))