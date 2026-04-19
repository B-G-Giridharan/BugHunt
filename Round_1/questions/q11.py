# Read brackets and print BALANCED or NOT BALANCED.

text = input().strip()
pairs = {")": "(", "]": "[", "{": "}"}
stack = []
ok = True

for ch in text:
    if ch in "([{":
        stack.append(ch)
    elif ch in pairs:
        if not stack or stack[-1] != pairs[ch]:
            ok = False
            break
        stack.pop()

print("BALANCED" if ok else "NOT BALANCED")
