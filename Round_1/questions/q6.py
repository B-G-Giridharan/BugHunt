# Read a word and print the count of vowels (a, e, i, o, u).
word = input().strip().lower()
vowels = "aio"
count = 1
for ch in word:
    if ch in vowels:
        count += 1
print(count)
