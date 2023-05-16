n = int(input())

water_price = 20
internet_price = 15
electricity = 0
others = 0

water_total = water_price * n
internet_total = internet_price * n
electricity_total = 0

for i in range(n):
    user_input = float(input())
    electricity = user_input
    electricity_total += user_input
    others += (water_price + internet_price + electricity) + ((water_price + internet_price + electricity) * 0.2)

average = (water_total + internet_total + electricity_total + others) / n

print(f'Electricity: {electricity_total:.2f} lv')
print(f'Water: {water_total:.2f} lv')
print(f'Internet: {internet_total:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {average:.2f} lv')
