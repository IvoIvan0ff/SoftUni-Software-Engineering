season = input()
group_type = input()
students_qty = int(input())
nights_qty = int(input())
price_per_night = 0
sport = ''

if group_type == 'boys' or group_type == 'girls':
    if season == 'Winter':
        price_per_night = 9.6
    elif season == 'Spring':
        price_per_night = 7.2
    else:
        price_per_night = 15
elif group_type == 'mixed':
    if season == 'Winter':
        price_per_night = 10
    elif season == 'Spring':
        price_per_night = 9.5
    else:
        price_per_night = 20

total_sum = (nights_qty * price_per_night) * students_qty

if students_qty >= 50:
    total_sum -= total_sum * 0.5
elif 20 <= students_qty < 50:
    total_sum -= total_sum * 0.15
elif 10 <= students_qty < 20:
    total_sum -= total_sum * 0.05

if group_type == 'girls':
    if season == 'Winter':
        sport = 'Gymnastics'
    elif season == 'Spring':
        sport = 'Athletics'
    else:
        sport = 'Volleyball'
elif group_type == 'boys':
    if season == 'Winter':
        sport = 'Judo'
    elif season == 'Spring':
        sport = 'Tennis'
    else:
        sport = 'Football'
else:
    if season == 'Winter':
        sport = 'Ski'
    elif season == 'Spring':
        sport = 'Cycling'
    else:
        sport = 'Swimming'

print(f'{sport} {total_sum:.2f} lv.')
