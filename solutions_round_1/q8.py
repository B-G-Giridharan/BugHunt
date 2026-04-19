phrase = input().strip()
cleaned = "".join(ch.lower() for ch in phrase if ch != " ")
if cleaned == cleaned[::-1]:
    print("YES")
else:
    print("NO")
