budget = int(input())
season = input()
fisherman_qty = int(input())
total_sum = 0
boat_rent = 0

if season == 'Spring':
    boat_rent = 3000
    if fisherman_qty <= 6:
        total_sum = boat_rent - boat_rent * 0.1
    elif 7 <= fisherman_qty <= 11:
        total_sum = boat_rent - boat_rent * 0.15
    elif fisherman_qty > 12:
        total_sum = boat_rent - boat_rent * 0.25
elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200
    if fisherman_qty <= 6:
        total_sum = boat_rent - boat_rent * 0.1
    elif 7 <= fisherman_qty <= 11:
        total_sum = boat_rent - boat_rent * 0.15
    elif fisherman_qty > 12:
        total_sum = boat_rent - boat_rent * 0.25
elif season == 'Winter':
    boat_rent = 2600
    if fisherman_qty <= 6:
        total_sum = boat_rent - boat_rent * 0.1
    elif 7 <= fisherman_qty <= 11:
        total_sum = boat_rent - boat_rent * 0.15
    elif fisherman_qty > 12:
        total_sum = boat_rent - boat_rent * 0.25
if fisherman_qty % 2 == 0:
    if season != 'Autumn':
        total_sum = total_sum - total_sum * 0.05
diff = abs(total_sum - budget)
if total_sum > budget:
    print(f'Not enough money! You need {diff:.2f} leva.')
else:
    print(f'Yes! You have {diff:.2f} leva left.')



