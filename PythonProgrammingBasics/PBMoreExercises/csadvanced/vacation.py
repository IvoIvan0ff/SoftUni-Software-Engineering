budget = float(input())
season = input()
location = ''
place = ''
price = 0

if budget <= 1000:
    place = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    else:
        location = 'Morocco'
        price = budget * 0.45
elif 100 < budget <= 3000:
    place = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.8
    else:
        location = 'Morocco'
        price = budget * 0.6
else:
    place = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.9
    else:
        location = 'Morocco'
        price = budget * 0.9

print(f'{location} - {place} - {price:.2f}')
