season = input()
km_per_month = float(input())
paycheck = 0
price_per_km = 0

if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.75
    elif season == 'Summer':
        price_per_km = 0.9
    else:
        price_per_km = 1.05
elif 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.95
    elif season == 'Summer':
        price_per_km = 1.1
    else:
        price_per_km = 1.25
elif 10000 < km_per_month <= 20000:
    price_per_km = 1.45
paycheck = (km_per_month * price_per_km) * 4
paycheck -= paycheck * 0.1

print(f'{paycheck:.2f}')
