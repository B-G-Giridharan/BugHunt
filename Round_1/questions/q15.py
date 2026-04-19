# Read a sentence and print the longest word (if tie, choose first).

words = input().strip().split(",")
best = ""

for word in words:
    if len(word) >= len(best):
        best = word

print(best)
