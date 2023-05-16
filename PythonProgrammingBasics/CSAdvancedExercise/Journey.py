budget = float(input())
season = input()
money_spent = 0
journey_type = ''
destination = ''

if budget <= 100:
    if season == 'summer':
        money_spent = budget * 0.3
        journey_type = 'Camp'
        destination = 'Bulgaria'
    elif season == 'winter':
        money_spent = budget * 0.7
        journey_type = 'Hotel'
        destination = 'Bulgaria'
elif 100 < budget <= 1000:
    if season == 'summer':
        money_spent = budget * 0.4
        journey_type = 'Camp'
        destination = 'Balkans'
    elif season == 'winter':
        money_spent = budget * 0.8
        journey_type = 'Hotel'
        destination = 'Balkans'
else:
    money_spent = budget * 0.9
    journey_type = 'Hotel'
    destination = 'Europe'

print(f'Somewhere in {destination}')
print(f'{journey_type} - {money_spent:.2f}')
