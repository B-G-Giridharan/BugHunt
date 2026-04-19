word = input().strip().lower()
vowels = "aeiou"
count = 0
for ch in word:
    if ch in vowels:
        count += 1
print(count)
