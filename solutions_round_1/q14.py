text = input().strip()
result = []
for ch in text:
    if "a" <= ch <= "z":
        result.append(chr((ord(ch) - ord("a") + 2) % 26 + ord("a")))
    elif "A" <= ch <= "Z":
        result.append(chr((ord(ch) - ord("A") + 2) % 26 + ord("A")))
    else:
        result.append(ch)
print("".join(result))
