month = input()
night_qty = int(input())
price_studio = 0
price_apart = 0
total_studio = 0
total_apart = 0

if month == 'May' or month == 'October':
    price_studio = 50
    price_apart = 65
    total_studio = night_qty * price_studio
    total_apart = night_qty * price_apart
    if 7 < night_qty <= 14:
        price_studio = price_studio - price_studio * 0.05
        total_studio = night_qty * price_studio
        total_apart = night_qty * price_apart

    elif night_qty > 14:
        price_studio = price_studio - price_studio * 0.3
        total_studio = night_qty * price_studio
        total_apart = night_qty * price_apart


elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apart = 68.70
    total_apart = night_qty * price_apart
    total_studio = night_qty * price_studio
    if night_qty > 14:
        price_studio = price_studio - price_studio * 0.2
        total_studio = night_qty * price_studio
elif month == 'July' or month == 'August':
    price_studio = 76
    price_apart = 77
    total_apart = night_qty * price_apart
    total_studio = night_qty * price_studio

if night_qty > 14:
    total_apart = total_apart - total_apart * 0.1

print(f'Apartment: {total_apart:.2f} lv.')
print(f'Studio: {total_studio:.2f} lv.')
