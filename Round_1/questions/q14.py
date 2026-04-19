# Read text and print Caesar-shifted text by +2 (preserve case).

text = input().strip()
result = []

for ch in text.lower():
    if "a" <= ch <= "z":
        shifted = chr((ord(ch) - ord("a") + 2) % 26 + ord("a"))
        result.append(shifted)
    else:
        result.append(ch + 1)

print("".join(result))
