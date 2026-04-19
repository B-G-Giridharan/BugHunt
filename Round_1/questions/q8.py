# Read a phrase and print YES if it is a palindrome (ignore spaces/case), else NO.

phrase = input().strip()
cleaned = phrase.lower()
if cleaned == cleaned[::-1]:
    print("YES")
else:
    print("NO")
