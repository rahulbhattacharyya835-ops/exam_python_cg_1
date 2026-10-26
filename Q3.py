products = {
    "Pen": 100,
    "Book": 300,
    "Bag": 500,
    "Pencil": 50,
    "Bottle": 150
}

def total_price(products):
    total = 0
    for price in products.values():
        total = total + price
    return total

print("Product List:")
for name, price in products.items():
    print(name, ":", price)

total = total_price(products)

if total >= 1000:
    discount = total * 10 / 100
else:
    discount = 0

bill = total - discount

print("Total Price:", total)
print("Discount:", discount)
print("Final Bill:", bill)