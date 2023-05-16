weight_in_kg = float(input())
type_service = input()
distance = int(input())

if type_service == 'standard':
    if weight_in_kg < 1:
        total_price = distance * 0.03
    elif 1 < weight_in_kg < 10:
        total_price = distance * 0.05
    elif 10 <= weight_in_kg < 40:
        total_price = distance * 0.1
    elif 40 <= weight_in_kg < 90:
        total_price = distance * 0.15
    elif 90 <= weight_in_kg < 150:
        total_price = distance * 0.2

else:
    if weight_in_kg < 1:
        total_price = distance * ((0.03 * 0.8 * weight_in_kg) + 0.03)
    elif 1 < weight_in_kg < 10:
        total_price = distance * ((0.05 * 0.4 * weight_in_kg) + 0.05)
    elif 10 <= weight_in_kg < 40:
        total_price = distance * ((0.1 * 0.05 * weight_in_kg) + 0.1)
    elif 40 <= weight_in_kg < 90:
        total_price = distance * ((0.15 * 0.02 * weight_in_kg) + 0.15)
    elif 90 <= weight_in_kg < 150:
        total_price = distance * ((0.2 * 0.01 * weight_in_kg) + 0.2)

print(f'The delivery of your shipment with weight of {weight_in_kg:.3f} kg. would cost {total_price:.2f} lv.')
