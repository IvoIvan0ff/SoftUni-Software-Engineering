orders_qty = int(input())
total = 0

for i in range(orders_qty):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_needed < 1 or capsules_needed > 2000:
        continue

    price = price_per_capsule * days * capsules_needed
    total += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total:.2f}")


