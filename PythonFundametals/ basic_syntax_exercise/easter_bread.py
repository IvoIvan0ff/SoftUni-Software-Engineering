budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price + (flour_price * 0.25)
colored_eggs = 0
bread_counter = 0
bread_price = eggs_price + flour_price + (milk_price * 0.25)

while budget > 0 and budget >= bread_price:
    budget -= bread_price
    colored_eggs += 3
    bread_counter += 1
    if bread_counter % 3 == 0:
        colored_eggs -= bread_counter - 2

print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
