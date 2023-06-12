items = input().split("|")
budget = float(input())
current_budget = budget
train_ticket = 150
new_prices = []
new_budget = 0
for i in items:
    item = i.split("->")
    type_of_item = item[0]
    item_price = float(item[1])
    if type_of_item == 'Clothes':
        if item_price <= budget:
            if item_price <= 50:
                budget -= item_price
                current_cloth_price = 0
                current_cloth_price = item_price + (item_price * 0.4)
                new_prices.append("%.2f" % current_cloth_price)
                new_budget += current_cloth_price
        else:
            continue
    elif type_of_item == 'Shoes':
        if item_price <= budget:
            if item_price <= 35:
                budget -= item_price
                current_shoe_price = 0
                current_shoe_price = item_price + (item_price * 0.4)
                new_prices.append("%.2f" % current_shoe_price)
                new_budget += current_shoe_price
        else:
            continue
    elif type_of_item == 'Accessories':
        if item_price <= budget:
            if item_price <= 20.50:
                budget -= item_price
                current_accessories_price = 0
                current_accessories_price = item_price + (item_price * 0.4)
                new_prices.append("%.2f" % current_accessories_price)
                new_budget += current_accessories_price
        else:
            continue
print(" ".join(new_prices))
print(f"Profit: {abs((budget + new_budget) - current_budget):.2f}")
if (budget + new_budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
