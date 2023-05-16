price_veg_kg = float(input())
price_fruit_kg = float(input())
total_veg_qty = int(input())
total_fruit_qty = int(input())

total_veg_price = (total_veg_qty * price_veg_kg) / 1.94
total_fruit_price = (total_fruit_qty * price_fruit_kg) / 1.94
total_price_eur = total_veg_price + total_fruit_price

print("%.2f" % total_price_eur)
