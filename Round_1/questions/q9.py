# Read item,qty and print total cost (10% discount only if qty >= 3).

prices = {"pen": 10, "book": 50, "bag": 200}
item, qty = [part.strip() for part in input().split(".")]
qty = float(qty)
total = prices[item] * qty
if qty >= 2:
    total = int(total * 0.9)
print(total)
