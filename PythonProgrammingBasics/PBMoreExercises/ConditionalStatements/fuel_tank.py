# Read User Input
fuel_type = input()
fuel_in_tank = float(input())

# Logic
if fuel_type == 'Diesel':
    if fuel_in_tank >= 25:
        print(f'You have enough {(fuel_type.lower())}.')
    elif fuel_in_tank < 25:
        print(f'Fill your tank with {(fuel_type.lower())}!')
elif fuel_type == 'Gasoline':
    if fuel_in_tank >= 25:
        print(f'You have enough {(fuel_type.lower())}.')
    elif fuel_in_tank < 25:
        print(f'Fill your tank with {(fuel_type.lower())}!')
elif fuel_type == 'Gas':
    if fuel_in_tank >= 25:
        print(f'You have enough {(fuel_type.lower())}.')
    elif fuel_in_tank < 25:
        print(f'Fill your tank with {(fuel_type.lower())}!')
else:
    print('Invalid fuel!')


# Output
