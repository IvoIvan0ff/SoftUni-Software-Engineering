budget = float(input())
extras_qty = int(input())
price_gear_per_extra = float(input())

decoration = budget * 0.1
discount = 0
total_price_extras = extras_qty * price_gear_per_extra

if extras_qty >= 150:
    discount = 0.1
    total_price_extras -= total_price_extras * discount

total_sum = total_price_extras + decoration
left_money = abs(budget - total_sum)

if total_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {left_money:.2f} leva more.")
else:
    print('Action!')
    print(f"Wingard starts filming with {left_money:.2f} leva left.")
