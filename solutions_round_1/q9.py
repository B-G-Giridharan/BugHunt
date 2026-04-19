prices = {"pen": 10, "book": 50, "bag": 200}
item, qty = [part.strip() for part in input().split(",")]
qty = int(qty)
total = prices[item] * qty
if qty >= 3:
    total = int(total * 0.9)
print(total)
