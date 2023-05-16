n = int(input())
price_per_ton = 0
total_baggage = 0
average_price = 0
total_cost = 0
p1, p2, p3 = 0, 0, 0

for i in range(n):
    user_input = int(input())
    if user_input <= 3:
        price_per_ton = 200
        total_baggage += user_input
        total_cost += user_input * price_per_ton
        p1 += user_input
    elif 4 <= user_input <= 11:
        price_per_ton = 175
        total_baggage += user_input
        total_cost += user_input * price_per_ton
        p2 += user_input
    else:
        price_per_ton = 120
        total_baggage += user_input
        total_cost += user_input * price_per_ton
        p3 += user_input

average_price = total_cost / total_baggage
p1_percentage = p1 / total_baggage * 100
p2_percentage = p2 / total_baggage * 100
p3_percentage = p3 / total_baggage * 100

print(f'{average_price:.2f}')
print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
